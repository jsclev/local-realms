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
