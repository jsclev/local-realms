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

store = Store(business=business, state_code='TN')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Bristol – The Pinnacle'
store.address1 = '4811 Old York Rd'
store.address2 = 'Unit 109'
store.city = 'Bristol'
store.zip_code = '37620'
store.latitude = 36.592526
store.longitude = -82.260995
store.save()

create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Johnson City', state_code='TN', zip_code='37601')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Johnson City – Johnson City Plaza Shopping Center'
store.address1 = '2116 N Roan St'
store.address2 = 'Suite 7'
store.latitude = 36.342768
store.longitude = -82.372622
store.save()

create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Kingsport', state_code='TN', zip_code='37660')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Kingsport – East Stone Commons'
store.address1 = '2003 N Eastman Rd'
store.address2 = 'Suite 36'
store.latitude = 36.543057
store.longitude = -82.517806
store.save()

create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
