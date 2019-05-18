import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business(name='Game Night Games')
business.website = 'www.gamenightgames.com'
business.save()

store = Store(business=business, city='Salt Lake City', state_code='UT', zip_code='84106')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '2148 South 900 East'
store.address2 = 'Ste 2'
store.latitude = 40.724268
store.longitude = -111.865636
store.save()
