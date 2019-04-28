import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business(name='Borderlands Comics and Games')
business.facebook = 'www.facebook.com/pages/Borderlands-Comics-and-Games/443080862461292'
business.save()

store = Store(business=business, city='Jacksonville', state_code='FL', zip_code='32225')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '10230 Atlantic Blvd'
store.street2 = '#11'
store.latitude = 30.322750
store.longitude = -81.534627
store.phone = '904-720-0774'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business(name='Friendly Local Game Store')
business.website = 'www.yourfriendlylocalgamestore.com'
business.facebook = 'www.facebook.com/FriendlyLocalGameStore'
business.email = 'lloyd@lloydwrites.com'
business.save()

store = Store(business=business, city='Jacksonville', state_code='FL', zip_code='32244')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '5517 Roosevelt Blvd'
store.latitude = 30.247073
store.longitude = -81.697058
store.phone = '904-503-8061'.replace('-', '')
store.save()
