from django.contrib import admin

from .models import State, Category, EmailTemplate, BrowseContent


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

class BrowseContentAdmin(admin.ModelAdmin):
    fields = ('state', 'category', 'meta_title', 'meta_description', 'meta_keywords', 'content' )
    list_display = ('id', 'state', 'category', 'meta_title', 'meta_description', 'meta_title', 'content' )

admin.site.register(BrowseContent, BrowseContentAdmin)
