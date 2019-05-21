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
business = Business.objects.get(name='Infinite Realities Comics & Games')
business.website = 'infiniterealitiescomics.com'
business.facebook = 'www.facebook.com/Infiniterealitiescomics'
business.save()

store = Store.objects.get(business=business)
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.phone = '470-359-5988'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-21T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-21T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-21T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-21T12:00:00+00:00')
