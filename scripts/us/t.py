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
business = Business.objects.get(name='cm games')
business.name = 'CM Games'
business.website = 'www.cardmonstergames.com'
business.facebook = 'https://www.facebook.com/CMGChattanooga'
business.email = 'cardmonstergames@gmail.com'
business.save()

store = Store.objects.get(business=business)
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '7401 E Brainerd Rd'
store.city = 'Chattanooga'
store.state_code = 'TN'
store.zip_code = '37421'
store.phone = '423-760-8429'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-23T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-23T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-23T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-23T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-23T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-23T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-23T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, state_code='TN')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'The Pinnacle'
store.address1 = '4811 Old York Rd'
store.address2 = 'Unit 109'
store.city = 'Bristol'
store.zip_code = '37620'
store.latitude = 36.592526
store.longitude = -82.260995
store.phone = '423-573-4263'.replace('-', '')
store.save()

create_store_log_item(store, STORE_STATUS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Johnson City', state_code='TN', zip_code='37601')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Johnson City Plaza Shopping Center'
store.address1 = '2116 N Roan St'
store.address2 = 'Suite 7'
store.latitude = 36.342768
store.longitude = -82.372622
store.phone = '423-915-1000'.replace('-', '')
store.save()

create_store_log_item(store, STORE_STATUS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Kingsport', state_code='TN', zip_code='37660')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'East Stone Commons'
store.address1 = '2003 N Eastman Rd'
store.address2 = 'Suite 36'
store.latitude = 36.543057
store.longitude = -82.517806
store.phone = '423-230-4263'.replace('-', '')
store.save()

create_store_log_item(store, STORE_STATUS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='Gamers Den')
business.website = 'www.247ttg.com'
business.facebook = 'https://www.facebook.com/gamersdencc'
business.save()

store = Store.objects.get(business=business)
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '6410 Weber Rd'
store.address2 = 'Suite 13'
store.city = 'Corpus Christi'
store.state_code = 'TX'
store.zip_code = '78413'
store.phone = '361-444-6607'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-22T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-22T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-22T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='Gardiners Games')
business.save()

store = Store.objects.get(business=business)
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.phone = '903-328-8610'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-22T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-22T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-22T12:00:00+00:00')
