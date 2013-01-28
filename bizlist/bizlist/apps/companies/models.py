from django.db import models
from django.template.defaultfilters import slugify

from references.models import State, Category

class Company(models.Model):

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    featured = models.BooleanField(default=False)
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    state = models.ForeignKey(State)
    address = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    person_in_charge = models.CharField(max_length=255, blank=True, null=True)
    person_position = models.CharField(max_length=255, blank=True, null=True)
    description_wanted = models.TextField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Company, self).save(*args, **kwargs)

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    description = models.TextField()
    company = models.ForeignKey(Company)
    category = models.ForeignKey(Category)
    price = models.CharField(max_length=255)
    price_remakrs = models.CharField(max_length=255, blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Company, self).save(*args, **kwargs)

class Photo(models.Model):
    picture = models.ImageField('Picture', blank=True, null=True, upload_to='photos/%Y/%m/%d')
    company = models.ForeignKey(Company, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

