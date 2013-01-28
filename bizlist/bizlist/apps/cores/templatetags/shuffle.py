#Shuffle a list in a template
import random
from django import template
register = template.Library()

@register.filter
def shuffle(arg, num=None):
    list_arg = list(arg)

    if num is not None:
        list_arg = random.sample(list_arg, num)

    else:
        random.shuffle(list_arg)

    return list_arg
