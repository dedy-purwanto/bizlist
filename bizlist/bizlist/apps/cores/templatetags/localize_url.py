from django import template
from django.template import TemplateSyntaxError
from django.template.defaulttags import kwarg_re, URLNode

register = template.Library()


class LocalizeURLNode(URLNode):

    def render(self, context):
        output = super(LocalizeURLNode, self).render(context)
        request = context['request']

        url = "/%s" % request.session['django_language']

        return (url + output)


@register.tag
def lurl(parser, token):

    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError("'%s' takes at least one argument"
                                  " (path to a view)" % bits[0])
    viewname = parser.compile_filter(bits[1])
    args = []
    kwargs = {}
    asvar = None
    bits = bits[2:]
    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]

    if len(bits):
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError("Malformed arguments to url tag")
            name, value = match.groups()
            if name:
                kwargs[name] = parser.compile_filter(value)
            else:
                args.append(parser.compile_filter(value))

    return LocalizeURLNode(viewname, args, kwargs, asvar, legacy_view_name=False)
