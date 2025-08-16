from django.urls import path

from . import views


app_name = 'lineo-pages'

urlpatterns = [
    # Pages
    ('', views.PageList, {}, 'page-list'),
    ('create/', views.PageCreate, {}, 'page-create'),
]

urlpatterns = [
    path(pattern, view.as_view(**kwargs), name=name)
    for pattern, view, kwargs, name in urlpatterns
]
