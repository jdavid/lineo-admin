# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic

from django_htmx import http as htmx
from formset.views import FormViewMixin

# Lineo
from .access import AccessMixin
from . import forms


app_name = 'lineo-admin'

User = get_user_model()

class Root(generic.RedirectView):
    url = reverse_lazy('lineo-admin:profile')

class Login(FormViewMixin, auth_views.LoginView):
    template_name = 'lineo_admin/anon/login.html'
    success_url = reverse_lazy('lineo-admin:profile')


class Logout(auth_views.LogoutView):
    http_method_names = ["post", "options", "get"]
    template_name = 'lineo_admin/anon/logout.html'

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if request.htmx:
            return htmx.HttpResponseClientRedirect(request.path)
        return response

class Profile(LoginRequiredMixin, generic.TemplateView):
    template_name = 'lineo_admin/profile.html'


class BaseListView(LoginRequiredMixin, generic.ListView):
    template_name = 'lineo_admin/list.html'
    create_viewname = None

    def get_columns(self):
        fields = []

        model = self.model
        for column in self.columns:
            field = model._meta.get_field(column)
            fields.append(field)

        return fields


class BaseCreateView(AccessMixin, FormViewMixin, generic.CreateView):
    template_name = 'lineo_admin/edit.html'

    def get_object(self):
        return None


class BaseUpdateView(AccessMixin, FormViewMixin, generic.UpdateView):
    template_name = 'lineo_admin/edit.html'


class BaseDeleteView(AccessMixin, FormViewMixin, generic.DeleteView):
    template_name = 'lineo_admin/delete.html'


class UserList(BaseListView):
    model = User
    create_viewname = f'{app_name}:user-create'

    columns = ['username', 'first_name', 'last_name']

    actions = [
        {'icon': 'trash', 'title': 'Delete', 'viewname': f'{app_name}:user-delete'},
        {'icon': 'edit', 'title': 'Edit', 'viewname': f'{app_name}:user-update'},
    ]

class UserCreate(BaseCreateView):
    access_verb = f'{app_name}:create_user'
    form_class = forms.UserForm
    model = User

class UserUpdate(BaseUpdateView):
    access_verb = f'{app_name}:update_user'
    form_class = forms.UserForm
    model = User

class UserDelete(BaseDeleteView):
    access_verb = f'{app_name}:delete_user'
    model = User

class UserProfile(AccessMixin, FormViewMixin, generic.UpdateView):
    access_verb = f'{app_name}:update_profile'
    form_class = forms.UserForm
    model = User
    template_name = 'lineo_admin/edit.html'

    def get_object(self, queryset=None):
        return self.request.user
