from django.forms.models import ModelForm
from . import models


class PageForm(ModelForm):
    class Meta:
        model = models.Page
        fields = '__all__'
