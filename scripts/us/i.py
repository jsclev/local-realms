import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


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

###############################################################################
# Business
###############################################################################
business = Business(name='Fair Game')
business.website = 'www.fairgamestore.com'
business.save()

store = Store(business=business, city='Downers Grove', state_code='IL', zip_code='60515')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '5147 Main St'
store.latitude = 41.793356
store.longitude = -88.010124
store.save()
