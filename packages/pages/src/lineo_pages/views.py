from lineo_admin import base
from lineo_admin.ui import Action

from . import forms, models


app_name = 'lineo-pages'

class PageList(base.ListView):
    model = models.Page
    create_viewname = f'{app_name}:page-create'

    columns = ['lang', 'path', 'title']

    actions = [
        Action(icon='circle-chevron-right', title='Read', viewname=f'{app_name}:page-read',
               drawer=False),
        Action(icon='trash', title='Delete', viewname=f'{app_name}:page-delete'),
    ]


class PageCreate(base.CreateView):
    access_verb = f'{app_name}:create_page'
    form_class = forms.PageForm
    model = models.Page


class PageRead(base.ReadView):
    access_verb = f'{app_name}:read_page'
    model = models.Page

class PageDelete(base.DeleteView):
    access_verb = f'{app_name}:delete_page'
    model = models.Page
