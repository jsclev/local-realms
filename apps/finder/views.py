from django.http import JsonResponse
from django.shortcuts import render

from apps.finder.models import Business
from apps.finder.serializers import BusinessSerializer


def get_home(request):
    return render(request, 'home.html', locals())


def get_shops(request):
    businesses = Business.objects.all()
    serializer = BusinessSerializer(businesses, many=True)

    return JsonResponse(serializer.data, safe=False)
