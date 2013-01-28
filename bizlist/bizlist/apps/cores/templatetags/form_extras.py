import re

from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


register = template.Library()


@register.filter
def render_label(field, arg=None):
    label = field.label

    if arg is not None:
        #label = label.replace("__replace_this__", arg)
        matches = re.match(r".*(__(\w+)__).*", label)
        if matches is not None:
            replace_this = matches.group(1)
            replace_label = str(getattr(arg, matches.group(2)))
            label = label.replace(replace_this, replace_label)
    
    field_html = u"<label for=\"id_%s\">%s" % (field.name, _(label))
    if field.errors:
        errors = [error for error in field.errors]
        field_html += u"<span class=\"errortext\">%s</span>" % "<br>".join(errors)
    field_html += "</label>"

    return mark_safe(field_html)
render_label.is_safe = True
