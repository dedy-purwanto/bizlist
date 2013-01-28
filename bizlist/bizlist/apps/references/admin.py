from django.contrib import admin

from .models import State, Category


class StateAdmin(admin.ModelAdmin):

    list_display = (
            'id',
            'title',
            'slug',
    )

admin.site.register(State, StateAdmin)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
            'id',
            'title',
            'slug',
            'meta_keywords',
            'meta_description',
            'parent',
    )

admin.site.register(Category, CategoryAdmin)
