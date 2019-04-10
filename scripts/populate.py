import django

django.setup()

from web.parties.models import Organization

org1 = Organization()
org1.name = 'Hello'
org1.save()
