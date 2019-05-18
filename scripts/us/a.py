import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store

###############################################################################
# Business
###############################################################################
business = Business(name='Amazing Discoveries')
business.website = 'www.amazingmtg.com'
business.facebook = 'www.facebook.com/AmazingDiscoveriesCG'
business.save()

store = Store(business=business, city='Casa Grande', state_code='AZ', zip_code='85122')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '204 N Sacaton St'
store.latitude = 32.877465
store.longitude = -111.755649
store.phone = '520-274-9294'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business(name='Friction Games')
business.website = 'www.frictiongamesaz.com'
business.facebook = 'www.facebook.com/frictiongamesaz'
business.save()

store = Store(business=business, city='Fort Huachuca', state_code='AZ', zip_code='85635')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '52035 Arizona St'
store.latitude = 31.557008
store.longitude = -110.352997
store.phone = '520-559-2202'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='Amazing Discoveries')

store = Store(business=business, city='Gilbert', state_code='AZ', zip_code='85234')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '745 N Gilbert Rd'
store.address2 = 'Ste 116'
store.latitude = 33.363882
store.longitude = -111.787992
store.phone = '520-460-6891'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='Amazing Discoveries')

store = Store(business=business, city='Tucson', state_code='AZ', zip_code='85719')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '2410 E Broadway Blvd'
store.latitude = 32.221302
store.longitude = -110.936149
store.phone = '520-320-0338'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business(name='Tucson Games and Gadgets')
business.website = 'www.tucsongamesandgadgets.com'
business.facebook = 'business.facebook.com/tucsongamesandgadgets'
business.email = 'tucsongamesandgadgets@gmail.com'
business.save()

store = Store(business=business, city='Tucson', state_code='AZ', zip_code='85711')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'Park Place Mall'
store.address1 = '5870 E Broadway Blvd'
store.address2 = '#110'
store.latitude = 32.219918
store.longitude = -110.866797
store.phone = '520-603-4037'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='Tucson Games and Gadgets')

store = Store(business=business, city='Tucson', state_code='AZ', zip_code='85705')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'Tucson Mall'
store.address1 = '4500 N Oracle'
store.address2 = '#253'
store.latitude = 32.288937
store.longitude = -110.975884
store.phone = '520-460-6891'.replace('-', '')
store.save()
