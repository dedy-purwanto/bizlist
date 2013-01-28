import re
from django import template

register = template.Library()

@register.filter
def replace_this(string, arg):

    if arg is not None:
        matches = re.match(r".*(__(\w+)__).*", string)
        if matches is not None:
            replace_this = matches.group(1)
            replace_label = str(getattr(arg, matches.group(2)))
            string = string.replace(replace_this, replace_label)

    return string
replace_this.is_safe = True


@register.filter
# truncate after a certain number of characters
def truncatechars(value, arg):
    if len(value) < arg:
        return value
    else:
        return value[:arg] + '...'

@register.filter
# truncate after a certain number of characters
def truncateemail(value, arg):
    if len(value) < arg:
        return value
    else:
        host = value.split("@").pop()
        return "%s@%s" % (truncatechars(value.split('@')[0], arg), host)
        #return value[:arg] + '...'
