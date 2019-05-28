from apps.finder.models import Business
from apps.finder.models import Store
from django.shortcuts import render
import settings


def get_no_phone_stores(request):
    version = settings.__version__

    businesses_with_no_website = Business.objects.filter(website='')
    num_businesses_with_no_website = businesses_with_no_website.count()

    stores_with_no_phone = Store.objects.filter(phone='')
    num_stores_with_no_phone = stores_with_no_phone.count()

    return render(request, 'maintenance.html', locals())
