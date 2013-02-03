from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify


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
