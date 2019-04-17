import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business(name='Fair Game')
business.website = 'www.fairgamestore.com'
business.save()

store = Store(business=business, city='Downers Grove', state_code='IL', zip_code='60515')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '5147 Main St'
store.latitude = 41.793356
store.longitude = -88.010124
store.save()
