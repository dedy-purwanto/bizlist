from django import template

register = template.Library()


class GenerateTitle(template.Node):

    def render(self, context):
        return u"Study abroad or locally"

@register.tag
def generate_title(parser, token):

    return GenerateTitle()
