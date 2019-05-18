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
business = Business(name='Borderlands Comics and Games')
business.facebook = 'www.facebook.com/pages/Borderlands-Comics-and-Games/443080862461292'
business.save()

store = Store(business=business, city='Jacksonville', state_code='FL', zip_code='32225')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '10230 Atlantic Blvd'
store.address2 = '#11'
store.latitude = 30.322750
store.longitude = -81.534627
store.phone = '904-720-0774'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Friendly Local Game Store')
business.website = 'www.yourfriendlylocalgamestore.com'
business.facebook = 'www.facebook.com/FriendlyLocalGameStore'
business.email = 'lloyd@lloydwrites.com'
business.save()

store = Store(business=business, city='Jacksonville', state_code='FL', zip_code='32244')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '5517 Roosevelt Blvd'
store.latitude = 30.247073
store.longitude = -81.697058
store.phone = '904-503-8061'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')
