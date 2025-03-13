from django.contrib.auth import views as auth_views
from django.views import generic
from django_htmx import http as htmx


class Login(auth_views.LoginView):
    template_name = 'lineo_admin/login.html'
    next_page = 'lineo-admin:profile'

class Logout(auth_views.LogoutView):
    template_name = 'lineo_admin/logout.html'

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return htmx.retarget(response, 'body')

class Profile(generic.TemplateView):
    template_name = 'lineo_admin/profile.html'
