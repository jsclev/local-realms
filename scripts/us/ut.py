import django

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business(name='Game Night Games')
business.website = 'www.gamenightgames.com'
business.save()

store = Store(business=business, state_code='UT')
store.street1 = '2148 South 900 East'
store.street2 = 'Ste 2'
store.city = 'Salt Lake City'
store.zip_code = '84106'
store.latitude = 40.724268
store.longitude = -111.865636
store.save()
