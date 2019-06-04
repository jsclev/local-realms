import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store
from scripts.functions import create_business_log_item
from scripts.functions import create_store_log_item

BUSINESS_STATUS = settings.GLOBAL_CONSTANTS['BUSINESS_STATUS']
BUSINESS_WEBSITE = settings.GLOBAL_CONSTANTS['BUSINESS_WEBSITE']
BUSINESS_EMAIL = settings.GLOBAL_CONSTANTS['BUSINESS_EMAIL']
BUSINESS_FACEBOOK = settings.GLOBAL_CONSTANTS['BUSINESS_FACEBOOK']
STORE_STATUS = settings.GLOBAL_CONSTANTS['STORE_STATUS']
STORE_ADDRESS = settings.GLOBAL_CONSTANTS['STORE_ADDRESS']
STORE_PHONE = settings.GLOBAL_CONSTANTS['STORE_PHONE']

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Abingdon', state_code='VA', zip_code='24210')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'Abingdon Towne Centre'
store.address1 = '376 Towne Centre Drive'
store.latitude = 36.701102
store.longitude = -81.977939
store.phone = '276-676-4263'.replace('-', '')
store.save()

create_store_log_item(store, STORE_STATUS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-21T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Huzzah Hobbies')
business.website = 'huzzahhobbies.com'
business.facebook = 'www.facebook.com/huzzah.hobbies.7'
business.save()

store = Store(business=business, city='Ashburn', state_code='VA', zip_code='20147')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '44927 George Washington Blvd'
store.latitude = 39.058097
store.longitude = -77.445812
store.phone = '703-466-0460'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='The Island Games')
business.website = 'www.theislandg.com'
business.facebook = 'www.facebook.com/theislandg'
business.email = 'contact@theislandg.com'
business.save()

store = Store(business=business, city='Centreville', state_code='VA', zip_code='20120')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'Sully Station Center'
store.address1 = '5107 Westfields Blvd'
store.latitude = 38.867360
store.longitude = -77.446814
store.phone = '515-599-0360'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='The End Games')
business.website = 'www.theendgames.co'
business.email = 'omegagamesllc@gmail.com'
business.facebook = 'https://www.facebook.com/TheEndGamesVA'
business.save()

store = Store(business=business, city='Charlottesville', state_code='VA', zip_code='22901')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '374 Hillsdale Dr'
store.latitude = 38.064315
store.longitude = -78.488559
store.phone = '434-973-2205'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='The Compleat Strategist')
business.website = 'www.thecompleatstrategist.com'
business.save()

store = Store(business=business, city='Falls Church', state_code='VA', zip_code='22046')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '103 E Broad St'
store.latitude = 38.882183
store.longitude = -77.170760
store.phone = '703-532-2477'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-19T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-19T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-19T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-19T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Victory Comics')
business.website = 'www.victorycomics.com'
business.facebook = 'www.facebook.com/VictoryComics'
business.email = 'victorycomics.fc@gmail.com'
business.save()

store = Store(business=business, city='Falls Church', state_code='VA', zip_code='22046')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '586 S Washington St'
store.latitude = 38.879380
store.longitude = -77.178619
store.phone = '703-241-9393'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Gamer Oasis')
business.facebook = 'www.facebook.com/GamerOasis'
business.save()

store = Store(business=business, city='Harrisonburg', state_code='VA', zip_code='22801')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'Cloverleaf Shopping Center'
store.address1 = '111 S Carlton St'
store.latitude = 38.441948
store.longitude = -78.855953
store.phone = '540-217-2672'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Just Games Lexington')
business.website = 'www.justgameslex.com'
business.email = 'zander@justgameslex.com'
business.save()

store = Store(business=business, city='Lexington', state_code='VA', zip_code='24450')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '314 S Main St'
store.latitude = 37.781786
store.longitude = -79.445417
store.phone = '540-724-6124'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Dragon Fire Games')
business.facebook = 'www.facebook.com/Dragon-Fire-Games-inc-1453584968210052'
business.save()

store = Store(business=business, city='Lynchburg', state_code='VA', zip_code='24501')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '3102 Memorial Ave'
store.latitude = 37.396347
store.longitude = -79.171051
store.phone = '434-229-3645'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Norton', state_code='VA', zip_code='24273')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Norton Commons'
store.address1 = '645 Commonwealth Dr'
store.latitude = 36.956268
store.longitude = -82.605011
store.phone = '276-679-1008'.replace('-', '')
store.save()

create_store_log_item(store, STORE_STATUS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')

###############################################################################
# Business
###############################################################################

business = Business(name='Atlantis Games & Comics')
business.website = 'www.atlantis-comics.com'
business.facebook = 'www.facebook.com/atlantis.games'
business.save()

store = Store(business=business, city='Norfolk', state_code='VA', zip_code='23503')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Atlantis Norfolk'
store.address1 = '9649 1st View St'
store.latitude = 36.955741
store.longitude = -76.254268
store.email = 'ac3@atlantis-comics.com'
store.facebook = 'www.facebook.com/atlantis.norfolk'
store.phone = '757-502-8954'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='Atlantis Games & Comics')

store = Store(business=business, city='Portsmouth', state_code='VA', zip_code='23701')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Atlantis Portsmouth'
store.address1 = '2862 Airline Blvd'
store.latitude = 36.810674
store.longitude = -76.368036
store.email = 'ac1@atlantis-comics.com'
store.facebook = 'www.facebook.com/atlantis.one'
store.phone = '757-465-1617'.replace('-', '')
store.save()

create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Game Quest Inc')
business.website = 'www.gamequestinc.com'
business.facebook = 'www.facebook.com/GameQuestInc'
business.email = 'gamequestinc@hotmail.com'
business.save()

store = Store(business=business, city='Radford', state_code='VA', zip_code='24141')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '1085 E Main St'
store.latitude = 37.140935
store.longitude = -80.556410
store.phone = '540-639-6547'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='One Eyed Jacques')
business.website = 'www.oejrva.com'
business.facebook = 'www.facebook.com/oneeyedjacques'
business.email = 'oej.contact@gmail.com'
business.save()

store = Store(business=business, city='Richmond', state_code='VA', zip_code='23221')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '3104 W Cary St'
store.latitude = 37.553151
store.longitude = -77.480305
store.phone = '804-359-5163'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Blade Gaming')
business.website = 'blade.tcgplayerpro.com'
business.facebook = 'www.facebook.com/BladeGaminginc'
business.email = 'tim.furrow@bladegaminginc.com'
business.save()

store = Store(business=business, city='Roanoke', state_code='VA', zip_code='24016')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '430 Salem Ave SW'
store.latitude = 37.272227
store.longitude = -79.949687
store.phone = '540-204-4016'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Mishap Games')
business.website = 'www.mishapgames.com'
business.facebook = 'www.facebook.com/mishapgames'
business.email = 'james@mishapgames.com'
business.save()

store = Store(business=business, city='Roanoke', state_code='VA', zip_code='24012')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '3432 Orange Ave NE'
store.latitude = 37.304304
store.longitude = -79.893189
store.phone = '540-342-1460'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Star City Game Center')
business.website = 'starcitygames.com'
business.facebook = 'www.facebook.com/scgamecenter'
business.save()

store = Store(business=business, city='Roanoke', state_code='VA', zip_code='24012')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '5728 Williamson Rd'
store.latitude = 37.328675
store.longitude = -79.954230
store.phone = '540-767-4263'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Tower of Games')
business.website = 'www.towerofgames.com'
business.facebook = 'www.facebook.com/towerofgames'
business.email = 'contactus@towerofgames.com'
business.save()

store = Store(business=business, city='Virginia Beach', state_code='VA', zip_code='23464')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '5405 Indian River Rd'
store.address2 = 'Suite A'
store.latitude = 36.798303
store.longitude = -76.178961
store.phone = '757-420-8008'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Kaboom')
business.website = 'kaboomgames.net'
business.facebook = 'www.facebook.com/KaboomVB'
business.email = 'kaboomvb@gmail.com'
business.save()

store = Store(business=business, city='Virginia Beach', state_code='VA', zip_code='23452')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '859 S Lynnhaven Rd'
store.latitude = 36.798303
store.longitude = -76.178961
store.phone = '757-301-9187'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='The Game Store')
business.website = 'www.thegamestore.online'
business.facebook = 'www.facebook.com/theGameStoreVa'
business.save()

store = Store(business=business, city='Warrenton', state_code='VA', zip_code='20186')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'Warrenton Village Center'
store.address1 = '251 W Lee Hwy'
store.address2 = 'Suite 655'
store.latitude = 38.730083
store.longitude = -77.799671
store.phone = '540-878-5480'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business.objects.get(name='G2K Games')

store = Store(business=business, city='Waynesboro', state_code='VA', zip_code='22980')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Gateway Park Shopping Center'
store.address1 = '1321 W Broad St'
store.latitude = 38.073755
store.longitude = -78.898431
store.phone = '540-943-4399'.replace('-', '')
store.save()

create_store_log_item(store, STORE_STATUS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-21T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Dark Mountain Games')
business.website = 'www.darkmountaingames.com'
business.email = 'darkmtngames@vermontel.net'
business.facebook = 'https://p.facebook.com/darkmountaingames'
business.save()

store = Store(business=business, city='Springfield', state_code='VT', zip_code='05156')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '27 Main St'
store.latitude = 43.299009
store.longitude = -72.482226
store.phone = '802-885-4800'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-05-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-05-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_EMAIL, '2019-05-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_FACEBOOK, '2019-05-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-05-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-05-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-05-18T12:00:00+00:00')

###############################################################################
# Business
###############################################################################
business = Business(name='Comic Kung Fu')
business.website = 'www.facebook.com/ComicKungFu'
business.save()

store = Store(business=business, city='Winchester', state_code='VA', zip_code='22601')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '672 N Loudoun St'
store.latitude = 39.195943
store.longitude = -78.160509
store.phone = '540-667-5497'.replace('-', '')
store.save()

create_business_log_item(business, BUSINESS_STATUS, '2019-04-18T12:00:00+00:00')
create_business_log_item(business, BUSINESS_WEBSITE, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_STATUS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_ADDRESS, '2019-04-18T12:00:00+00:00')
create_store_log_item(store, STORE_PHONE, '2019-04-18T12:00:00+00:00')
