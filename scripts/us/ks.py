import django

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business(name='Asgards Gate')
business.website = 'https://asgardsgate.website'
business.facebook = 'https://www.facebook.com/asgardsgateholton'
business.save()

store = Store(business=business, state_code='KS')
store.street1 = '106 W 5th St'
store.street2 = None
store.city = 'Holton'
store.zip_code = '66436'
store.latitude = 39.465175
store.longitude = -95.735196
store.save()
