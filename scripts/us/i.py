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
business = Business(name='First Turn Games')
business.website = 'www.firstturngames.com'
business.facebook = 'www.facebook.com/FirstTurnGames'
business.save()

store = Store(business=business, city='Cedar Rapids', state_code='IA', zip_code='52402')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '3645 1st Ave SE'
store.latitude = 42.015345
store.longitude = -91.633349
store.phone = '319-826-1289'.replace('-', '')
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
business = Business(name='Tempest Games LLC')
business.website = 'tempestgames.net'
business.facebook = 'www.facebook.com/TempestGames'
business.email = 'rich@tempestgames.net'
business.save()

store = Store(business=business, city='Cedar Rapids', state_code='IA', zip_code='52405')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Tempest Games'
store.address1 = '212 Edgewood Rd NW'
store.address2 = 'Suite K'
store.latitude = 41.973420
store.longitude = -91.716889
store.phone = '319-390-6441'.replace('-', '')
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
business = Business(name='All About Games')
business.website = 'allaboutgames.com'
business.save()

store = Store(business=business, city='Boise', state_code='ID', zip_code='83709')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Overland Location'
store.address1 = '7079 W Overland Rd'
store.latitude = 43.589194
store.longitude = -116.269873
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
store = Store(business=business, city='Boise', state_code='ID', zip_code='83702')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Downtown Location'
store.address1 = '120 N 8th St'
store.latitude = 43.615762
store.longitude = -116.203093
store.save()

create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
store = Store(business=business, city='Boise', state_code='ID', zip_code='83704')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Mall Location'
store.address1 = '350 N Milwaukee St'
store.latitude = 43.608643
store.longitude = -116.278262
store.save()

create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Fair Game')
business.website = 'www.fairgamestore.com'
business.email = 'fairgamestore@gmail.com'
business.facebook = 'www.facebook.com/fairgamestore'
business.save()

store = Store(business=business, city='Downers Grove', state_code='IL', zip_code='60515')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '5147 Main St'
store.latitude = 41.793356
store.longitude = -88.010124
store.phone = '630-963-0640'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-20T12:00:00+00:00')
