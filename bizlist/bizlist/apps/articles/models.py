from django.db import models
from django.template.defaultfilters import slugify

class Article(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

