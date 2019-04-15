import django

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business(name='The End Games')
business.website = 'www.theendgames.co'
business.save()

store = Store(business=business, state_code='VA')
store.street1 = '374 Hillsdale Dr'
store.city = 'Charlottesville'
store.zip_code = '22901'
store.latitude = 38.064315
store.longitude = -78.488559
store.save()

business = Business(name='Dragon Fire Games')
business.website = 'www.facebook.com/Dragon-Fire-Games-inc-1453584968210052'
business.save()

store = Store(business=business, state_code='VA')
store.street1 = '3102 Memorial Ave'
store.city = 'Lynchburg'
store.zip_code = '24501'
store.latitude = 37.396347
store.longitude = -79.171051
store.save()

business = Business(name='The Island Games')
business.website = 'www.theislandg.com'
business.save()

store = Store(business=business, state_code='VA')
store.street1 = '5107 Westfields Blvd'
store.city = 'Centreville'
store.zip_code = '20120'
store.latitude = 38.867360
store.longitude = -77.446814
store.save()

business = Business(name='The Compleat Strategist')
business.website = 'www.thecompleatstrategist.com'
business.save()

store = Store(business=business, state_code='VA')
store.street1 = '103 E Broad St'
store.city = 'Falls Church'
store.zip_code = '22046'
store.latitude = 38.882183
store.longitude = -77.170760
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, state_code='VA')
store.name = 'Abingdon – Towne Centre'
store.street1 = '376 Towne Centre Drive'
store.city = 'Abingdon'
store.zip_code = '24210'
store.latitude = 36.701102
store.longitude = -81.977939
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, state_code='VA')
store.name = 'Norton – Norton Commons'
store.street1 = '645 Commonwealth Dr'
store.city = 'Norton'
store.zip_code = '24273'
store.latitude = 36.956268
store.longitude = -82.605011
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, state_code='VA')
store.name = 'Kingsport – East Stone Commons'
store.street1 = '2003 N Eastman Rd'
store.street2 = 'Suite 36'
store.city = 'Kingsport'
store.zip_code = '37660'
store.latitude = 36.543057
store.longitude = -82.517806
store.save()

business = Business.objects.get(name='G2K Games')

store = Store(business=business, state_code='VA')
store.name = 'Waynesboro – Gateway Park Shopping Center'
store.street1 = '1321 W Broad St'
store.city = 'Waynesboro'
store.zip_code = '22980'
store.latitude = 38.073755
store.longitude = -78.898431
store.save()
