from apps.finder.models import Business
from apps.finder.models import Store
from django.shortcuts import render
import settings


def get_no_phone_stores(request):
    businesses_with_no_website = Business.objects.filter(website='')
    stores_with_no_phone = Store.objects.filter(phone='')
    version = settings.__version__

    return render(request, 'maintenance/maintenance.html', locals())
