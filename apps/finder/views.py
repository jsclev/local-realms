from django.conf import settings as django_settings
from django.http import JsonResponse
from django.shortcuts import render

import settings
from apps.finder.models import Business
from apps.finder.serializers import BusinessSerializer
from apps.finder.models import Tag
from apps.finder.serializers import TagSerializer


def get_home(request):
    version = settings.__version__
    mapbox_access_token = django_settings.GLOBAL_CONSTANTS['MAPBOX_ACCESS_TOKEN']

    return render(request, 'home.html', locals())


def get_about(request):
    version = settings.__version__

    return render(request, 'about.html', locals())


def get_contact(request):
    version = settings.__version__

    return render(request, 'contact.html', locals())


def get_shops(request):
    businesses = Business.objects.all().order_by('name',
                                                 )
    serializer = BusinessSerializer(businesses, many=True)

    return JsonResponse(serializer.data, safe=False)


def get_tags(request):
    tags = Tag.objects.all().order_by('name')
    serializer = TagSerializer(tags, many=True)

    return JsonResponse(serializer.data, safe=False)
