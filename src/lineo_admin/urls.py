from django.urls import path

from . import views


app_name = 'lineo-admin'

urlpatterns = [
    ('', views.Root, 'root'),
    ('login/', views.Login, 'login'),
    ('logout/', views.Logout, 'logout'),
    ('profile/', views.Profile, 'profile'),
]

urlpatterns = [
    path(pattern, view.as_view(), name=name)
    for pattern, view, name in urlpatterns
]
