from django.contrib import admin
from django import forms
from fields.googlemapsearch import GoogleMapsWidget

from .models import Company, Product, Photo

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

class CompanyAdmin(admin.ModelAdmin):

    form = CompanyForm

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
