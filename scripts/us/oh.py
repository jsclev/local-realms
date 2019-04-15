import django

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business.objects.create(name='Frogtown Hobbies')
store = Store(business=business, state_code='OH')
store.street1 = '27250 Crossroad Parkway a'
store.street2 = None
store.city = 'Rossford'
store.zip_code = '43460'
store.latitude = 41.546179
store.longitude = -83.582045
store.save()
