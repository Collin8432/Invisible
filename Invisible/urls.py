
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("search", views.search, name="search"),
    path("searching", views.searching, name="searching"),
    
    path("admin/discordoauth", views.discordoauth, name="admin/discordoauth"),
    path("admin/authed", views.authed, name="admin/authed"),
    
    path("chat", views.chat, name="chat"),
]
