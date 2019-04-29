import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business(name='Enchanted Realms Games and Gifts')
business.website = 'www.enchantedrealmsgames.com'
business.facebook = 'www.facebook.com/PetriesGames'
business.save()

store = Store(business=business, city='Colorado Springs', state_code='CO', zip_code='80910')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '1050 S Academy Blvd'
store.latitude = 38.817881
store.longitude = -104.758201
store.phone = '719-418-2187'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business(name="Petrie's Family Games")
business.website = 'www.petriesgames.com'
business.facebook = 'www.facebook.com/PetriesGames'
business.save()

store = Store(business=business, city='Colorado Springs', state_code='CO', zip_code='80920')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '7681 N Union Blvd'
store.latitude = 38.942139
store.longitude = -104.774062
store.phone = '719-522-1099'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business(name="Gamer's Haven")
business.website = 'www.gamershavenco.com'
business.facebook = 'www.facebook.com/GamersHavenCO'
business.save()

store = Store(business=business, city='Colorado Springs', state_code='CO', zip_code='80918')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '5730 N Academy Blvd'
store.latitude = 38.913907
store.longitude = -104.788893
store.phone = '719-531-9863'.replace('-', '')
store.save()

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
store.street1 = '521 Chinook Ln'
store.latitude = 38.287747
store.longitude = -104.599527
store.phone = '719-542-1237'.replace('-', '')
store.save()
