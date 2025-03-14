from django import template


register = template.Library()

@register.simple_tag
def get(obj, name):
    return getattr(obj, name)
