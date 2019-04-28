import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business(name='Asgards Gate')
business.website = 'asgardsgate.website'
business.facebook = 'www.facebook.com/asgardsgateholton'
business.save()

store = Store(business=business, city='Holton', state_code='KS', zip_code='66436')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '106 W 5th St'
store.latitude = 39.465175
store.longitude = -95.735196
store.save()

###############################################################################
# Business
###############################################################################
business = Business(name='Gatekeeper Hobbies')
business.website = 'www.gatekeeperhobbies.com'
business.facebook = 'www.facebook.com/GatekeeperHobbies'
business.save()

store = Store(business=business, city='Topeka', state_code='KS', zip_code='66604')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'Gage Shopping Center'
store.street1 = '4123 SW Gage Center Dr'
store.latitude = 39.042176
store.longitude = -95.727563
store.phone = '785-232-3429'.replace('-', '')
store.save()
