from django.conf import settings as django_settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

import settings
from apps.finder.models import Business, Store, UserStoreSuggestion
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


def add_store(request):
    if request.method == "POST":
        post_values = request.POST

        name = post_values['name']
        address1 = post_values['address']
        address2 = post_values['address-line-2']
        city = post_values['city']
        state = post_values['state']
        zip_code = post_values['zip-code']
        latitude = post_values['latitude']
        longitude = post_values['longitude']
        phone = post_values['phone']
        website = post_values['website']
        facebook = post_values['facebook']
        email = post_values['email']


        if address2 is None:
            address2 = ''

        else:
            suggestion = UserStoreSuggestion()
            if not request.user.is_anonymous:
                suggestion.user = request.user
            suggestion.name = name
            suggestion.website = website
            suggestion.facebook = facebook
            suggestion.email = email
            suggestion.phone = phone
            suggestion.address1 = address1
            suggestion.address2 = address2
            suggestion.city = city
            suggestion.state = state
            suggestion.zip_code = zip_code
            if suggestion.latitude:
                suggestion.latitude = latitude
            if suggestion.longitude:
                suggestion.longitude = longitude
            suggestion.save()

    return redirect('/')