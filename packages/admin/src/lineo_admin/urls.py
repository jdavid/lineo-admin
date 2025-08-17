from django.urls import path

from . import views


app_name = 'lineo-admin'

urlpatterns = [
    ('', views.Root, {}, 'root'),
    ('login/', views.Login,{},  'login'),
    ('logout/', views.Logout, {}, 'logout'),
    ('profile/', views.Profile, {}, 'profile'),
    ('user/profile/', views.UserProfile, {}, 'user-profile'),
    # Users
    ('users/', views.UserList, {}, 'user-list'),
    ('users/create/', views.UserCreate, {}, 'user-create'),
    ('users/<int:pk>/update/', views.UserUpdate, {}, 'user-update'),
    ('users/<int:pk>/delete/', views.UserDelete, {}, 'user-delete'),
]

urlpatterns = [
    path(pattern, view.as_view(**kwargs), name=name)
    for pattern, view, kwargs, name in urlpatterns
]
