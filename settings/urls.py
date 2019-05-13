from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.urls import path

from apps.finder import views
from settings.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^robots.txt',
        lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"),
        name="robots_file"),

    path('admin/', admin.site.urls),
    path('', views.get_home, name='main'),
    path('about', views.get_about, name='about'),
    path('contact', views.get_contact, name='contact'),
    path('shops/', views.get_shops),
    path('tags/', views.get_tags),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
