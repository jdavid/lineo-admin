from django.forms.boundfield import BoundField
from django.forms.utils import ErrorList
from django import template
from django.template.loader import render_to_string


register = template.Library()

@register.simple_tag
def tw(obj, placeholder=''):
    if type(obj) is ErrorList:
        template = 'lineo_admin/tw/error_list.html'
        context = {'errors': obj}
    elif type(obj) is BoundField:
        assert obj.use_fieldset is False
        #breakpoint()
        #.widget.attrs
        #.legend
        #.css_classes
        #.data
        #.errors
        #.help_text
        #.is_hidden
        template = 'lineo_admin/tw/field.html'
        context = {'field': obj, 'placeholder': placeholder}
    else:
        raise TypeError(f'Unexpected {type(obj)}')

    return render_to_string(template, context)
