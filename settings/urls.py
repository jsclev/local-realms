from django.contrib import admin
from django.urls import path

from apps.finder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_home),
    path('about/', views.get_about),
    path('contact/', views.get_contact),
    path('shops/', views.get_shops),
    path('tags/', views.get_tags)
]
