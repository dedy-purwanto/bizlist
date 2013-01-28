from django.contrib import admin

from .models import Company, Product, Photo


class CompanyAdmin(admin.ModelAdmin):

    list_display = (
            'id',
            'title',
    )

admin.site.register(Company, CompanyAdmin)


class ProductAdmin(admin.ModelAdmin):

    list_display = (
            'id',
            'title',
            'company'
    )

admin.site.register(Product, ProductAdmin)


class PhotoAdmin(admin.ModelAdmin):

    list_display = (
            'id',
            'company'
    )

admin.site.register(Photo, PhotoAdmin)
