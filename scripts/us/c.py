import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business(name='All About Games')
business.website = 'allaboutgames.com'
business.facebook = 'www.facebook.com/AllAboutGames365'
business.save()

store = Store(business=business, city='Boise', state_code='ID', zip_code='83709')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Overland Location'
store.street1 = '7079 W Overland Rd'
store.latitude = 43.589194
store.longitude = -116.269873
store.phone = '208-343-5653'.replace('-', '')
store.save()
