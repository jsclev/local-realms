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
business = Business.objects.create(name='Battleground Games And Hobbies')
business.facebook = 'www.facebook.com/FantasyGameCenter'
business.save()

store = Store(business=business, city='Port Clinton', state_code='OH', zip_code='43452')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '114 E Perry St'
store.latitude = 41.512950
store.longitude = -82.940332
store.phone = '419-341-8753'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Frogtown Hobbies')
business.website = 'www.frogtownhobbies.com'
business.email = 'rob@frogtownhobbies.com'
business.facebook = 'https://www.facebook.com/FrogtownHobbies'
business.save()

store = Store(business=business, city='Rossford', state_code='OH', zip_code='43460')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '27250 Crossroad Parkway'
store.address2 = 'Unit A'
store.latitude = 41.546179
store.longitude = -83.582045
store.phone = '567-331-1535'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-22T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-22T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-22T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-22T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='Games Galore')
business.facebook = 'https://www.facebook.com/gamesgalorecolumbus'
business.save()

store = Store.objects.get(business=business)
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.phone = '614-383-7028'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-22T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-22T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-22T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='Multiverse Comics & Beyond')
business.facebook = 'https://www.facebook.com/MultiverseComicsAndBeyond'
business.save()

store = Store.objects.get(business=business)
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.phone = '419-277-8318'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-22T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-22T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-22T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-22T12:00:00+00:00')
