from django.contrib import admin
from django import forms
from fields.googlemapsearch import GoogleMapsWidget
from tinymce.widgets import TinyMCE

from .models import Company, Product, Photo, Inquiry

class CompanyForm(forms.ModelForm):
    latitude = forms.CharField(label="Map",widget = GoogleMapsWidget(
        attrs={'map_canvas':'map_canvas','width': 450, 'height': 300,
            'longitude_id':'id_longitude',
            'city_id': 'id_city', 'country_id': 'id_country',
            'state_id': 'id_state', 'address_id':'id_address'}),

        error_messages={'required': 'Please select point from the map.'})
    longitude = forms.CharField(widget = forms.HiddenInput())

    class Meta:

        model = Company
        widgets = {
            'description' : TinyMCE(attrs={'cols':80, 'rows' : 10}),
            'description_wanted' : TinyMCE(attrs={'cols':80, 'rows' : 10}),
        }


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product
        widgets = {
            'description' : TinyMCE(attrs={'cols':80, 'rows' : 10}),
        }

class CompanyAdmin(admin.ModelAdmin):

    form = CompanyForm

    list_display = (
            'id',
            'title',
    )

admin.site.register(Company, CompanyAdmin)


class ProductAdmin(admin.ModelAdmin):

    form = ProductForm

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

class InquiryAdmin(admin.ModelAdmin):

    list_display = (
            'id',
            'name',
            'email'
    )

admin.site.register(Inquiry, InquiryAdmin)
