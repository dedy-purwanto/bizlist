from urllib import urlencode
from django import template

register = template.Library()

def paginator(context, adjacent_pages=0):

    current_page = context['page_obj'].number
    start_page = current_page - adjacent_pages if current_page > adjacent_pages else 1
    num_pages = context['paginator'].num_pages
    end_page = current_page + adjacent_pages \
                   if current_page + adjacent_pages < num_pages else num_pages

    page_numbers = [n for n in xrange(start_page, end_page + 1)]

    context['page_numbers'] = page_numbers
    return context

register.inclusion_tag("paginator.html", takes_context=True)(paginator)


@register.filter
def page_url(value, arg):
    if isinstance(value, dict):
        get_dict = value.copy()
    else:
        get_dict = {}

    get_dict['page'] = arg
    return urlencode(get_dict)
