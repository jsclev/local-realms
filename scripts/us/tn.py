import django

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business.objects.get(name='G2K Games')

store = Store(business=business, state_code='TN')
store.name = 'Bristol – The Pinnacle'
store.street1 = '4811 Old York Rd'
store.street2 = 'Unit 109'
store.city = 'Bristol'
store.zip_code = '37620'
store.latitude = 36.592526
store.longitude = -82.260995
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, state_code='TN')
store.name = 'Johnson City – Johnson City Plaza Shopping Center'
store.street1 = '2116 N Roan St'
store.street2 = 'Suite 7'
store.city = 'Johnson City'
store.zip_code = '37601'
store.latitude = 36.342768
store.longitude = -82.372622
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, state_code='TN')
store.name = 'Kingsport – East Stone Commons'
store.street1 = '2003 N Eastman Rd'
store.street2 = 'Suite 36'
store.city = 'Kingsport'
store.zip_code = '37660'
store.latitude = 36.543057
store.longitude = -82.517806
store.save()
