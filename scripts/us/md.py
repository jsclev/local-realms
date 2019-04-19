import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business.objects.create(name='High Tide Games')
business.website = 'www.hightidegames.com'
business.facebook = 'www.facebook.com/HighTideGames'
business.email = 'hightidegames@yahoo.com'
business.save()

store = Store(business=business, city='California', state_code='MD', zip_code='20619')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'San Souci Plaza'
store.street1 = '22599 MacArthur Blvd'
store.street2 = 'Suite #126'
store.latitude = 38.288438
store.longitude = -76.486903
store.phone = '240-587-0791'.replace('-', '')
store.save()
