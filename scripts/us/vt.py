import django

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business(name='Dark Mountain Games')
business.website = 'http://www.darkmountaingames.com'
business.email = 'darkmtngames@vermontel.net'
business.save()

store = Store(business=business, state_code='VT')
store.street1 = '27 Main St'
store.city = 'Springfield'
store.zip_code = '05156'
store.latitude = 43.299009
store.longitude = -72.482226
store.save()
