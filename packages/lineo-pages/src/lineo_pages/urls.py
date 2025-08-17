from django.urls import path

from . import views


app_name = 'lineo-pages'

urlpatterns = [
    # Pages
    ('', views.PageList, {}, 'page-list'),
    ('create/', views.PageCreate, {}, 'page-create'),
    ('delete/<int:pk>/', views.PageDelete, {}, 'page-delete'),
]

urlpatterns = [
    path(pattern, view.as_view(**kwargs), name=name)
    for pattern, view, kwargs, name in urlpatterns
]
