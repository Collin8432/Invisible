
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("admin/", views.admin, name="admin"),
    path("admin/discordoauth", views.discordoauth, name="admin/discordoauth"),
    path("admin/authed", views.authed, name="admin/authed"),
    
    path("admin/login", views.login, name="login"),
]
