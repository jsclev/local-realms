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
business = Business(name='Game Night Games')
business.website = 'www.gamenightgames.com'
business.email = 'info@gamenightgames.com'
business.facebook = 'https://www.facebook.com/gamenightgames'
business.save()

store = Store(business=business, city='Salt Lake City', state_code='UT', zip_code='84106')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '2148 South 900 East'
store.address2 = 'Suite 2'
store.latitude = 40.724268
store.longitude = -111.865636
store.phone = '801-467-2400'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-20T12:00:00+00:00')
