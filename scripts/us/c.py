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
business = Business.objects.get(name='+EV Games')
business.name = 'Plus EV Games'
business.website = 'www.plusevgames.com'
business.facebook = 'www.facebook.com/plusevgames'
business.email = 'sales@plusevgames.com'
business.save()

store = Store.objects.get(business=business)
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '300 N Lantana St'
store.address2 = 'Ste #38'
store.city = 'Camarillo'
store.state_code = 'CA'
store.zip_code = '93010'
store.phone = '805-389-7428'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-13T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-13T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-13T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-13T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-13T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-13T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-13T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Enchanted Realms Games and Gifts')
business.website = 'www.enchantedrealmsgames.com'
business.facebook = 'www.facebook.com/PetriesGames'
business.save()

store = Store(business=business, city='Colorado Springs', state_code='CO', zip_code='80910')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '1050 S Academy Blvd'
store.latitude = 38.817881
store.longitude = -104.758201
store.phone = '719-418-2187'.replace('-', '')
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
business = Business(name="Petrie's Family Games")
business.website = 'www.petriesgames.com'
business.facebook = 'www.facebook.com/PetriesGames'
business.save()

store = Store(business=business, city='Colorado Springs', state_code='CO', zip_code='80920')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '7681 N Union Blvd'
store.latitude = 38.942139
store.longitude = -104.774062
store.phone = '719-522-1099'.replace('-', '')
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
business = Business(name="Gamer's Haven")
business.website = 'www.gamershavenco.com'
business.facebook = 'www.facebook.com/GamersHavenCO'
business.save()

store = Store(business=business, city='Colorado Springs', state_code='CO', zip_code='80918')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '5730 N Academy Blvd'
store.latitude = 38.913907
store.longitude = -104.788893
store.phone = '719-531-9863'.replace('-', '')
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
business = Business(name='Chaos Games and More')
business.website = 'www.chaosgamesandmore.com'
business.facebook = 'www.facebook.com/chaosgamesandmore'
business.email = 'john@chaosgamesandmore.com'
business.save()

store = Store(business=business, city='Pueblo', state_code='CO', zip_code='81001')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '521 Chinook Ln'
store.latitude = 38.287747
store.longitude = -104.599527
store.phone = '719-542-1237'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')
