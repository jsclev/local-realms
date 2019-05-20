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
business = Business.objects.create(name='Your Local Game Store')
business.website = 'www.yourlocalgamestore.com'
business.email = 'contact@yourlocalgamestore.com'
business.facebook = 'https://www.facebook.com/Your-Local-Game-Store-364969030246513'
business.save()

store = Store(business=business, city='Mint Hill', state_code='NC', zip_code='28227')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '6908 Matthews-Mint Hill Rd'
store.address2 = 'Suite 350'
store.latitude = 35.171643
store.longitude = -80.657079
store.phone = '704-729-4547'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-20T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Hillside Games and Comics')
business.facebook = 'www.facebook.com/HillsideGames'
business.save()

store = Store(business=business, city='Asheville', state_code='NC', zip_code='28803')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'River Ridge Market Pl'
store.address1 = '800 Fairview Rd'
store.address2 = 'Suite EE'
store.latitude = 35.570199
store.longitude = -82.507587
store.phone = '828-505-1195'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-20T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Carolina Tabletop Games')
business.facebook = 'www.facebook.com/carolinatabletopgames'
business.save()

store = Store(business=business, city='Pineville', state_code='NC', zip_code='28134')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '315 Main St'
store.address2 = '#1'
store.latitude = 35.085479
store.longitude = -80.890651
store.phone = '704-835-1128'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-20T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Spandex City')
business.website = 'spandexcity.com'
business.facebook = 'https://www.facebook.com/SpandexCity'
business.save()

store = Store(business=business, city='Charlotte', state_code='NC', zip_code='28214')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '2914 Mt Holly-Huntersville Rd'
store.latitude = 35.319121
store.longitude = -80.952932
store.phone = '704-909-7168'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-19T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-19T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-19T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-19T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-19T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-19T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-19T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name="The Wyvern's Tale")
business.website = 'www.thewyvernstaleavl.com'
business.facebook = 'https://www.facebook.com/thewyvernstale'
business.email = 'store@TheWyvernsTaleAVL.com'
business.save()

store = Store(business=business, city='Asheville', state_code='NC', zip_code='28801')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '347 Merrimon Ave'
store.latitude = 35.610936
store.longitude = -82.554662
store.phone = '828-505-7887'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-19T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-19T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-19T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-19T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-19T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-19T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-19T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='The Deck Box')
business.website = 'www.thedeckbox.com'
business.facebook = 'https://www.facebook.com/thedeckboxcards'
business.save()

store = Store(business=business, city='Fletcher', state_code='NC', zip_code='28732')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '3049 Hendersonville Rd'
store.address2 = 'Suite 30'
store.latitude = 35.439584
store.longitude = -82.504974
store.phone = '828-681-1861'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-20T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-20T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-20T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='G2K Games')
business.website = 'www.g2kgames.net'
business.save()

store = Store(business=business, city='Morganton', state_code='NC', zip_code='28655')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Morganton – Morganton Heights Shopping Center'
store.address1 = 'E150 Morganton Heights Blvd'
store.latitude = 35.725135
store.longitude = -81.704035
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
