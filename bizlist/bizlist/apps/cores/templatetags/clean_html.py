from django import template
from hescar_utils.strings import CleanHTML
register = template.Library()

@register.filter
def clean_html(arg):
    return CleanHTML(arg)

