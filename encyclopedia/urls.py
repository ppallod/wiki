from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("newitem/", views.newitem, name="newitem"),
    path("edit/<str:title>", views.edit,name="edit"),
    path("search/", views.search, name="search"),
    path("randompage/", views.randompage, name="randompage"),
    path("wiki/<str:title>/", views.entry, name="entry")
]
