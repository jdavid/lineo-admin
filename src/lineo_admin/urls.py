from django.urls import path

from . import views


app_name = 'lineo-admin'

urlpatterns = [
    ('login/', views.Login, 'login'),
]

urlpatterns = [
    path(pattern, view.as_view(), name=name)
    for pattern, view, name in urlpatterns
]
