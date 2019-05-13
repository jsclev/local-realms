from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return ['main', 'about', 'contact']

    def location(self, item):
        return reverse(item)
