import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business(name='Labyrinth Games & Puzzles')
business.website = 'labyrinthgameshop.com'
business.facebook = 'www.facebook.com/labyrinthgameshop'
business.save()

store = Store(business=business, city='Washington', state_code='DC', zip_code='20003')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '645 Pennsylvania Ave SE'
store.latitude = 38.884565
store.longitude = -76.996953
store.phone = '202-544-1059'.replace('-', '')
store.save()
