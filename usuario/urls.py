from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("menu/", views.menu, name="menu"),
    path("logout/", views.logout_view, name="logout"),
]