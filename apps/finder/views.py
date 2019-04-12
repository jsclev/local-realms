from django.http import JsonResponse
from django.shortcuts import render

from apps.finder.models import Organization
from apps.finder.serializers import OrganizationSerializer


def get_home(request):
    return render(request, 'home.html', locals())


def get_shops(request):
    # serializer = DriverScheduleSerializer(driver_schedules, many=True)
    #
    # return JsonResponse(serializer.data, safe=False)

    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)

    return JsonResponse(serializer.data, safe=False)
