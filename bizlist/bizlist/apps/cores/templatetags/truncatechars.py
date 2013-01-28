from django import template

register = template.Library()

@register.filter
def truncatechars(string, length):
    if len(string) <= length:
        return string
    return "%s..." % string[0:length]
