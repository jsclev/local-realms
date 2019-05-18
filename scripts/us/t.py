import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, state_code='TN')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Bristol – The Pinnacle'
store.address1 = '4811 Old York Rd'
store.address2 = 'Unit 109'
store.city = 'Bristol'
store.zip_code = '37620'
store.latitude = 36.592526
store.longitude = -82.260995
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Johnson City', state_code='TN', zip_code='37601')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Johnson City – Johnson City Plaza Shopping Center'
store.address1 = '2116 N Roan St'
store.address2 = 'Suite 7'
store.latitude = 36.342768
store.longitude = -82.372622
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Kingsport', state_code='TN', zip_code='37660')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Kingsport – East Stone Commons'
store.address1 = '2003 N Eastman Rd'
store.address2 = 'Suite 36'
store.latitude = 36.543057
store.longitude = -82.517806
store.save()
