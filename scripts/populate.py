import django

django.setup()

from apps.finder.models import Organization
from apps.finder.models import PostalAddress

Organization.objects.all().delete()

org = Organization.objects.create(name='Your Local Game Store')
pa = PostalAddress(organization=org, state_code='NC')
pa.street1 = '6908 Matthews-Mint Hill Rd'
pa.street2 = 'Suite 350'
pa.city = 'Mint Hill'
pa.zip_code = '28227'
pa.save()

org = Organization.objects.create(name='Hillside Games and Comics')
pa = PostalAddress(organization=org, state_code='NC')
pa.street1 = '800 Fairview Rd'
pa.street2 = 'Suite EE'
pa.city = 'Asheville'
pa.zip_code = '28803'
pa.save()

