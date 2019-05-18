import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store
from scripts.functions import create_business_log_item
from scripts.functions import create_store_log_item

BUSINESS_STATUS = settings.GLOBAL_CONSTANTS['BUSINESS_STATUS']
BUSINESS_WEBSITE = settings.GLOBAL_CONSTANTS['BUSINESS_WEBSITE']
BUSINESS_EMAIL = settings.GLOBAL_CONSTANTS['BUSINESS_EMAIL']
BUSINESS_FACEBOOK = settings.GLOBAL_CONSTANTS['BUSINESS_FACEBOOK']
STORE_STATUS = settings.GLOBAL_CONSTANTS['STORE_STATUS']
STORE_ADDRESS = settings.GLOBAL_CONSTANTS['STORE_ADDRESS']
STORE_PHONE = settings.GLOBAL_CONSTANTS['STORE_PHONE']

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Rock Hill', state_code='SC', zip_code='29732')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Rock Hill – Wal-Mart Shopping Center'
store.address1 = '4811 Old York Rd'
store.address2 = 'Suite 102'
store.latitude = 34.981058
store.longitude = -81.090907
store.save()

create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Rock Hill', state_code='SC', zip_code='29730')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Rock Hill – Rock Hill Galleria'
store.address1 = '2301 Dave Lyle Blvd'
store.address2 = 'Suite 117'
store.latitude = 34.943390
store.longitude = -80.965526
store.save()

create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
