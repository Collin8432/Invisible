
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio", views.portfolio, name="portfolio"),
    
    path("admin/discordoauth", views.discordoauth, name="admin/discordoauth"),
    path("admin/authed", views.authed, name="admin/authed"),
    path("login", views.login, name="login"),
]
