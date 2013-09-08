import itertools
from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


class State(models.Model):

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)

    def get_products(self):
        from companies.models import Product
        products = Product.objects.filter(company__state=self).distinct()
        return products
        

    def __unicode__(self):
        return "%s" % self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(State, self).save(*args, **kwargs)
    

class Category(models.Model):

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)

    # Called from parent category, fetch list of company attached 
    # to this category along with its subcategory
    def get_companies(self):
        from companies.models import Company
        companies = Company.objects.filter(
                Q(categories=self) |
                Q(categories__parent=self)
                ).distinct()
        return companies

    def get_products(self):
        from companies.models import Product
        products = Product.objects.filter(
                Q(category=self) |
                Q(category__parent=self)
                ).distinct()
        return products

    def __unicode__(self):
        return "%s" % self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class EmailTemplate(models.Model):

    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    template = models.TextField()
    template_html = models.TextField(blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)

        return super(EmailTemplate, self).save()

    def __unicode__(self):
        return "%s" % self.name


class BrowseContent(models.Model):
    state = models.ForeignKey(State, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    meta_title = models.CharField(max_length=1024, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        #Making sure no such permutation already exist if this is a new one
        if not self.pk:
            try:
                content = BrowseContent.objects.get(
                        state=self.state,
                        category=self.category)
                raise Exception("BrowseContent object with this permutation is already exists: %s" % (content.pk))
            except BrowseContent.DoesNotExist:
                pass

        return super(BrowseContent, self).save(*args, **kwargs)

    def generate_default_values(self):

        state = self.state
        category = self.category
        state_title = state if state else "Myanmar"
        category_title = category if category else "All"

        if not state and not category:
            meta_title = "Browse directory of Myanmar manufacturers, exporters, importers and other businesses"
        else:
            meta_title = "%s companies in %s" % (category_title, state_title)

        meta_keywords = "%s companies in myanmar,  %s companies in burma,  %s importers in myanmar,  %s importers in burma,  %s manufacturers in myanmar,  %s manufacturers in burma, %s manufacturers, importers and exporters in %s, myanmar businesses, myanmar companies, myanmar directory of companies, myanmar directory of businesses, myanmar directory of manufacturers" % (category_title, category_title, \
                category_title, category_title, category_title, category_title, category_title,\
                state_title)

        meta_descriptions = "Comprehensive list of manufacturers, importers and exporters in %s in %s, Myanmar / Burma." % (category_title if category else '', state_title if state else '')

        self.meta_title = meta_title
        self.meta_keywords = meta_keywords
        self.meta_description = meta_descriptions
        self.save()


    @staticmethod
    def create_content(state=None, category=None):
        try:
            content = BrowseContent.objects.get(state=state, category=category)
        except BrowseContent.DoesNotExist:
            content = BrowseContent()
            content.state = state
            content.category = category
            content.save()

        content.generate_default_values()
            

    @staticmethod
    def rebuild_permutation(delete_all=False):
        states = [s for s in State.objects.all().order_by('title')]
        categories = [c for c in Category.objects.all().order_by('title')]

        if delete_all:
            BrowseContent.objects.all().delete()

        for p in list(itertools.product(states)): 
            BrowseContent.create_content(state=p[0])

        for p in list(itertools.product(categories)): 
            BrowseContent.create_content(category=p[0])

        for p in list(itertools.product(states, categories)): 
            BrowseContent.create_content(state=p[0], category=p[1])


#@receiver(post_save, sender=BrowseContent)
#def user_post_save(sender, instance, created, **kwargs):
    #BrowseContent.rebuild_permutation(delete_all=False)
