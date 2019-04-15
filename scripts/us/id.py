import django

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business(name='All About Games')
business.website = 'allaboutgames.com'
business.save()

store = Store(business=business, state_code='ID')
store.name = 'Overland Location'
store.street1 = '7079 W Overland Rd'
store.city = 'Boise'
store.zip_code = '83709'
store.latitude = 43.589194
store.longitude = -116.269873
store.save()

store = Store(business=business, state_code='ID')
store.name = 'Downtown Location'
store.street1 = '120 N 8th St'
store.city = 'Boise'
store.zip_code = '83702'
store.latitude = 43.615762
store.longitude = -116.203093
store.save()

store = Store(business=business, state_code='ID')
store.name = 'Mall Location'
store.street1 = '350 N Milwaukee St'
store.city = 'Boise'
store.zip_code = '83704'
store.latitude = 43.608643
store.longitude = -116.278262
store.save()
