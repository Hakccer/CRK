from django.contrib import admin
from django.urls import path, include
from first import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile', views.profile, name="profile"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('addpass', views.add_pass, name="add_pass"),
    path('delpass', views.del_pass, name="del_pass"),
    path('editpass/<slug:slug>', views.edit_pass, name="edit_pass"),
    path('room', views.room, name="Room"),
    path("room/<slug:slug>", views.sluggu, name="sluggu"),
    path('send', views.send, name="send")
]
