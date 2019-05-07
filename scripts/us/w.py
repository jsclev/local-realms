import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business(name='Your Hobby Place')
business.website = 'www.yourhobbyplace.com'
business.facebook = 'www.facebook.com/YourHobbyPlace'
business.email = 'sales@yourhobbyplace.com'
business.save()

store = Store(business=business, city='Martinsburg', state_code='WV', zip_code='25404')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '77 Monroe St'
store.latitude = 39.482063
store.longitude = -77.950841
store.phone = '304-267-3110'.replace('-', '')
store.save()
