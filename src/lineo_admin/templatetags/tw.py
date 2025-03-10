from django.forms.boundfield import BoundField
from django import template


register = template.Library()


@register.inclusion_tag('lineo_admin/field.html')
def tw(field, placeholder=''):
    if type(field) is not BoundField:
        raise TypeError(f'Unexpected {type(field)}')

    assert field.use_fieldset is False
    #breakpoint()
    #.widget.attrs
    #.legend
    #.css_classes
    #.data
    #.errors
    #.help_text
    #.is_hidden

    return {'field': field, 'placeholder': placeholder}
