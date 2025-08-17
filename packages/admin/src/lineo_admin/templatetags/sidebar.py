from django import template
from .. import registry


register = template.Library()

@register.inclusion_tag('lineo_admin/sidebar-items.html')
def sidebar_items():
    return {
        'items': registry.sidebar.get_items()
    }
