from django.contrib.auth import views as auth_views


class Login(auth_views.LoginView):
    template_name = 'lineo_admin/login.html'
