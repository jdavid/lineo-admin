from django import template
from django.urls import resolve, reverse

from lineo_admin.access import access


register = template.Library()

@register.simple_tag(takes_context=True)
def urlaccess(context, viewname, obj):
    request = context['request']
    user = request.user

    kwargs = {'pk': obj.pk}
    url = reverse(viewname, kwargs=kwargs)
    match = resolve(url)
    verb = match.func.view_class.access_verb
    if access.is_allowed(user, verb, obj):
        return url
    return None
