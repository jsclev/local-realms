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
business = Business(name='Mind Sculpt Games')
business.website = 'www.mindsculptgames.com'
business.facebook = 'www.facebook.com/mindsculptgames'
business.email = 'mindsculptgames@gmail.com'
business.save()

store = Store(business=business, city='Great Bend', state_code='KS', zip_code='67530')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '2521 10th St'
store.latitude = 38.361049
store.longitude = -98.772931
store.phone = '620-603-8462'.replace('-', '')
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
business = Business(name='Asgards Gate')
business.website = 'asgardsgate.website'
business.facebook = 'www.facebook.com/asgardsgateholton'
business.save()

store = Store(business=business, city='Holton', state_code='KS', zip_code='66436')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '106 W 5th St'
store.latitude = 39.465175
store.longitude = -95.735196
store.phone = '785-362-6346'.replace('-', '')
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
business = Business(name="The Dragon's Hoard")
business.website = 'www.dragonshoardllc.com'
business.facebook = 'www.facebook.com/TheDragonsHoardLLC'
business.save()

store = Store(business=business, city='Lawrence', state_code='KS', zip_code='66044')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '1045 Pennsylvania St'
store.latitude = 38.963988
store.longitude = -95.229401
store.phone = '785-766-9608'.replace('-', '')
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
business = Business(name='Gatekeeper Hobbies')
business.website = 'www.gatekeeperhobbies.com'
business.facebook = 'www.facebook.com/GatekeeperHobbies'
business.save()

store = Store(business=business, city='Topeka', state_code='KS', zip_code='66604')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'Gage Shopping Center'
store.address1 = '4123 SW Gage Center Dr'
store.latitude = 39.042176
store.longitude = -95.727563
store.phone = '785-232-3429'.replace('-', '')
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
business = Business(name="Grog's Games, Play Space and Board Game Club")
business.facebook = 'www.facebook.com/grogsgames'
business.save()

store = Store(business=business, city='Topeka', state_code='KS', zip_code='66614')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '3124 SW 29th St'
store.address2 = '#8'
store.latitude = 39.015418
store.longitude = -95.716992
store.phone = '785-221-7164'.replace('-', '')
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
business = Business(name="Huscarl Hobbies and Games")
business.website = 'www.huscarlhobbiesandgames.com'
business.facebook = 'www.facebook.com/HuscarlHobbies'
business.email = 'contactus@huscarlhobbiesandgames.com'
business.save()

store = Store(business=business, city='Topeka', state_code='KS', zip_code='66604')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '1930 SW Westport Dr'
store.latitude = 39.031604
store.longitude = -95.756133
store.phone = '785-215-6545'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')
