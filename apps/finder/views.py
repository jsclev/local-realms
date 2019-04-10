from django.shortcuts import render

from apps.finder.models import Organization


def get_home(request):
    organizations = Organization.objects.all()

    return render(request, 'home.html', locals())
