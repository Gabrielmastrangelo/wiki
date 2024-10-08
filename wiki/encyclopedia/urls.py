from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_page, name="title"),
    path("search", views.search, name="search"),
    path('newpage', views.new_page, name="new_page"),
    path('edit/<str:title>', views.edit, name="edit"),
    path('random', views.random, name="random")
]
