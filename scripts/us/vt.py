import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business(name='Dark Mountain Games')
business.website = 'www.darkmountaingames.com'
business.email = 'darkmtngames@vermontel.net'
business.save()

store = Store(business=business, city='Springfield', state_code='VT', zip_code='05156')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '27 Main St'
store.latitude = 43.299009
store.longitude = -72.482226
store.save()
