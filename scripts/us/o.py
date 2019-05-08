import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Battleground Games And Hobbies')
business.facebook = 'www.facebook.com/FantasyGameCenter'
business.save()

store = Store(business=business, city='Port Clinton', state_code='OH', zip_code='43452')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '114 E Perry St'
store.latitude = 41.512950
store.longitude = -82.940332
store.phone = '419-341-8753'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Frogtown Hobbies')

store = Store(business=business, city='Rossford', state_code='OH', zip_code='43460')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '27250 Crossroad Parkway a'
store.latitude = 41.546179
store.longitude = -83.582045
store.save()
