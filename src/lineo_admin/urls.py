from django.urls import path

from . import views


app_name = 'lineo-admin'

urlpatterns = [
    ('', views.Root, {}, 'root'),
    ('login/', views.Login,{},  'login'),
    ('logout/', views.Logout, {}, 'logout'),
    ('profile/', views.Profile, {}, 'profile'),
    ('users/', views.UserList, {}, 'user-list'),
    ('users/create/', views.UserCreate, {}, 'user-create'),
    ('users/update/<int:pk>/', views.UserUpdate, {}, 'user-update'),
    ('users/delete/<int:pk>/', views.UserDelete, {}, 'user-delete'),
    ('user/profile/', views.UserProfile, {}, 'user-profile'),
]

urlpatterns = [
    path(pattern, view.as_view(**kwargs), name=name)
    for pattern, view, kwargs, name in urlpatterns
]
