from django.contrib.auth import views as auth_views
from django.views import generic


class Login(auth_views.LoginView):
    template_name = 'lineo_admin/login.html'
    next_page = 'lineo-admin:profile'

class Logout(auth_views.LogoutView):
    template_name = 'lineo_admin/logout.html'

class Profile(generic.TemplateView):
    template_name = 'lineo_admin/profile.html'
