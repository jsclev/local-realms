from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from apps.finder import views

urlpatterns = [
    url(r'^robots.txt',
        lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"),
        name="robots_file"),
    path('admin/', admin.site.urls),
    path('', views.get_home),
    path('about/', views.get_about),
    path('contact/', views.get_contact),
    path('shops/', views.get_shops),
    path('tags/', views.get_tags)
]
