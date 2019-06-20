
from django.urls import path

from apps.maintenance import views
from settings.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.maintenance),
    path('view_incomplete/', views.get_no_phone_stores),
    path('view_suggestions/', views.view_user_suggestions)
]