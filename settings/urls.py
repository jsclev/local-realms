from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.urls import path, include

from apps.finder import views
from apps.accounts import views as account_views
from apps.maintenance import views as maintenance_views
from settings.sitemaps import StaticViewSitemap
import django.contrib.auth.urls

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^robots.txt',
        lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type='text/plain'),
        name='robots_file'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', views.get_home, name='main'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', account_views.SignUp.as_view(), name='signup'),
    path('about/', views.get_about, name='about'),
    path('contact/', views.get_contact, name='contact'),
    path('shops/', views.get_shops),
    path('tags/', views.get_tags),
    path('maintenance/', maintenance_views.get_no_phone_stores)
]
