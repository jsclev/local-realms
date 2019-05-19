from apps.finder.models import Store
from django.shortcuts import render
import settings


def get_no_phone_stores(request):
    stores = Store.objects.filter(phone='')
    version = settings.__version__

    return render(request, 'maintenance/no_phones.html', locals())
