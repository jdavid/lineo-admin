from lineo_admin.views import BaseListView, BaseCreateView, BaseDeleteView

from . import forms
from . import models


app_name = 'lineo-pages'

class PageList(BaseListView):
    model = models.Page
    create_viewname = f'{app_name}:page-create'

    columns = ['lang', 'path', 'title']

    actions = [
        {'icon': 'trash', 'title': 'Delete', 'viewname': f'{app_name}:page-delete'},
#       {'icon': 'edit', 'title': 'Edit', 'viewname': f'{app_name}:page-update'},
    ]


class PageCreate(BaseCreateView):
    access_verb = f'{app_name}:create_page'
    form_class = forms.PageForm
    model = models.Page

class PageDelete(BaseDeleteView):
    access_verb = f'{app_name}:delete_page'
    model = models.Page
