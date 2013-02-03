from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify

from references.models import State, Category, EmailTemplate
from emails import send_using_template

class Company(models.Model):

    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    featured = models.BooleanField(default=False)
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='companies')
    state = models.ForeignKey(State, related_name='companies')
    address = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    person_in_charge = models.CharField(max_length=255, blank=True, null=True)
    person_position = models.CharField(max_length=255, blank=True, null=True)
    description_wanted = models.TextField(blank=True, null=True)
    picture = models.ImageField('Picture', blank=True, null=True, upload_to='companies/%Y/%m/%d')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Company, self).save(*args, **kwargs)

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    description = models.TextField()
    company = models.ForeignKey(Company, related_name='products')
    category = models.ForeignKey(Category, related_name='products')
    price = models.CharField(max_length=255)
    price_remarks = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField('Picture', blank=True, null=True, upload_to='products/%Y/%m/%d')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

class Photo(models.Model):
    picture = models.ImageField('Picture', blank=True, null=True, upload_to='photos/%Y/%m/%d')
    company = models.ForeignKey(Company, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company)
    product = models.ForeignKey(Product, blank=True, null=True)

    def send_email(self, send_thankyou=True):
        context = { 
                'inquiry' : self,
        }
        template = EmailTemplate.objects.get(slug='inquiry')
        send_using_template(template, context, self.company.email)

        if send_thankyou:
            self.send_email_thankyou()

    def send_email_thankyou(self):
        context = { 
                'inquiry' : self,
        }

        template = EmailTemplate.objects.get(slug='inquiry-thank-you')
        send_using_template(template, context, self.email)

