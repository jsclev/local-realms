import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business(name='The End Games')
business.website = 'www.theendgames.co'
business.save()

store = Store(business=business, city='Charlottesville', state_code='VA', zip_code='22901')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '374 Hillsdale Dr'
store.latitude = 38.064315
store.longitude = -78.488559
store.save()

business = Business(name='Dragon Fire Games')
business.website = 'www.facebook.com/Dragon-Fire-Games-inc-1453584968210052'
business.save()

store = Store(business=business, city='Lynchburg', state_code='VA', zip_code='24501')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '3102 Memorial Ave'
store.latitude = 37.396347
store.longitude = -79.171051
store.save()

business = Business(name='The Island Games')
business.website = 'www.theislandg.com'
business.save()

store = Store(business=business, city='Centreville', state_code='VA', zip_code='20120')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '5107 Westfields Blvd'
store.latitude = 38.867360
store.longitude = -77.446814
store.save()

business = Business(name='The Compleat Strategist')
business.website = 'www.thecompleatstrategist.com'
business.save()

store = Store(business=business, city='Falls Church', state_code='VA', zip_code='22046')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.street1 = '103 E Broad St'
store.latitude = 38.882183
store.longitude = -77.170760
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Abingdon', state_code='VA', zip_code='24210')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Abingdon – Towne Centre'
store.street1 = '376 Towne Centre Drive'
store.latitude = 36.701102
store.longitude = -81.977939
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Norton', state_code='VA', zip_code='24273')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Norton – Norton Commons'
store.street1 = '645 Commonwealth Dr'
store.latitude = 36.956268
store.longitude = -82.605011
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Kingsport', state_code='VA', zip_code='37660')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Kingsport – East Stone Commons'
store.street1 = '2003 N Eastman Rd'
store.street2 = 'Suite 36'
store.latitude = 36.543057
store.longitude = -82.517806
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Waynesboro', state_code='VA', zip_code='22980')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Waynesboro – Gateway Park Shopping Center'
store.street1 = '1321 W Broad St'
store.latitude = 38.073755
store.longitude = -78.898431
store.save()

business = Business(name='The Game Store')
business.website = 'www.thegamestore.online'
business.facebook = 'www.facebook.com/theGameStoreVa'
business.save()

store = Store(business=business, city='Warrenton', state_code='VA', zip_code='20186')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'Warrenton Village Center'
store.street1 = '251 W Lee Hwy'
store.street2 = 'suite 655'
store.latitude = 38.730083
store.longitude = -77.799671
store.save()
