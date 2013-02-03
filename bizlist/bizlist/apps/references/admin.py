from django.contrib import admin

from .models import State, Category, EmailTemplate


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

class EmailTemplateAdmin(admin.ModelAdmin):
    fields = ('name', 'subject', 'template', 'template_html', )

    list_display = (
            'id',
            'name',
            'slug',
    )

admin.site.register(EmailTemplate, EmailTemplateAdmin)
