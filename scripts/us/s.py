import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Rock Hill', state_code='SC', zip_code='29732')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Rock Hill – Wal-Mart Shopping Center'
store.street1 = '4811 Old York Rd'
store.street2 = 'Suite 102'
store.latitude = 34.981058
store.longitude = -81.090907
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Rock Hill', state_code='SC', zip_code='29730')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Rock Hill – Rock Hill Galleria'
store.street1 = '2301 Dave Lyle Blvd'
store.street2 = 'Suite 117'
store.latitude = 34.943390
store.longitude = -80.965526
store.save()
