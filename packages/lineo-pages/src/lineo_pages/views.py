from lineo_admin.views import BaseListView, BaseCreateView

from . import forms
from . import models


class PageList(BaseListView):
    model = models.Page
    create_viewname = 'lineo-pages:page-create'

    columns = ['lang', 'path', 'title']

    actions = [
#       {'icon': 'trash', 'title': 'Delete', 'viewname': 'lineo-admin:user-delete'},
#       {'icon': 'edit', 'title': 'Edit', 'viewname': 'lineo-admin:user-update'},
    ]


class PageCreate(BaseCreateView):
    access_verb = 'create_user'
    form_class = forms.PageForm
    model = models.Page
