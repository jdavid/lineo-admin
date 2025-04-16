# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic

from django_htmx import http as htmx
from formset.views import FormViewMixin

# Lineo
from . import forms


User = get_user_model()

class Root(generic.RedirectView):
    url = reverse_lazy('lineo-admin:profile')

class Login(auth_views.LoginView):
    template_name = 'lineo_admin/login.html'
    next_page = 'lineo-admin:profile'

class Logout(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'lineo_admin/logout.html'

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return htmx.retarget(response, 'body')

class Profile(LoginRequiredMixin, generic.TemplateView):
    template_name = 'lineo_admin/profile.html'


class BaseListView(LoginRequiredMixin, generic.ListView):

    def get_columns(self):
        fields = []

        model = self.model
        for column in self.columns:
            field = model._meta.get_field(column)
            fields.append(field)

        return fields

class UserList(BaseListView):
    model = User
    template_name = 'lineo_admin/list.html'

    columns = [
        'username', 'first_name', 'last_name',
    ]

    actions = [
        {'icon': 'icons/edit.svg', 'title': 'Edit', 'viewname': 'lineo-admin:user-update'},
        {'icon': 'icons/delete.svg', 'title': 'Delete', 'viewname': 'lineo-admin:user-delete'},
    ]

class UserCreate(LoginRequiredMixin, FormViewMixin, generic.CreateView):
    form_class = forms.UserForm
    model = User
    template_name = 'lineo_admin/edit.html'

class UserUpdate(LoginRequiredMixin, FormViewMixin, generic.UpdateView):
    form_class = forms.UserForm
    model = User
    template_name = 'lineo_admin/edit.html'

class UserDelete(LoginRequiredMixin, FormViewMixin, generic.DeleteView):
    form_class = forms.UserForm
    model = User
    template_name = 'lineo_admin/edit.html'
