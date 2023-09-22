from django.urls import path
from userapp import views

urlpatterns=[
    path("register",views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.loguot, name="logout"),
]