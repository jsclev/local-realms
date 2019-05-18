import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='High Tide Games')
business.website = 'www.hightidegames.com'
business.facebook = 'www.facebook.com/HighTideGames'
business.email = 'hightidegames@yahoo.com'
business.save()

store = Store(business=business, city='California', state_code='MD', zip_code='20619')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.location_heading = 'San Souci Plaza'
store.address1 = '22599 MacArthur Blvd'
store.address2 = 'Suite #126'
store.latitude = 38.288438
store.longitude = -76.486903
store.phone = '240-587-0791'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='The Board and Brew')
business.website = 'www.theboardandbrew.com'
business.facebook = 'www.facebook.com/TheBoardAndBrew'
business.save()

store = Store(business=business, city='College Park', state_code='MD', zip_code='20740')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '8150 Baltimore Ave'
store.latitude = 38.288438
store.longitude = -76.486903
store.phone = '240-542-4613'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Arkham Games')
business.facebook = 'www.facebook.com/arkhamgames'
business.save()

store = Store(business=business, city='Cumberland', state_code='MD', zip_code='21502')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '1068 National Hwy'
store.latitude = 39.640022
store.longitude = -78.827243
store.phone = '304-209-1413'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Check Us First')
business.website = 'checkusfirst.tcgplayerpro.com'
business.facebook = 'www.facebook.com/CheckUsFirst'
business.email = 'checkus1st@gmail.com'
business.save()

store = Store(business=business, city='Damascus', state_code='MD', zip_code='20872')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '26212 Ridge Rd'
store.latitude = 39.287753
store.longitude = -77.207540
store.phone = '240-207-3651'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Brainstorm Comics & Gaming')
business.website = 'www.brainstormcomics.com'
business.facebook = 'www.facebook.com/brainstormcomix'
business.email = 'info@brainstormcomics.com'
business.save()

store = Store(business=business, city='Frederick', state_code='MD', zip_code='21701')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '54 E Patrick St'
store.latitude = 39.414004
store.longitude = -77.409187
store.phone = '301-663-3039'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Tournament City Games')
business.website = 'www.tournamentcitygames.com'
business.facebook = 'www.facebook.com/TournamentCityGames'
business.email = 'TournamentCityGames@gmail.com'
business.save()

store = Store(business=business, city='Frederick', state_code='MD', zip_code='21701')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '467 W Patrick St'
store.address2 = 'Suite 8a'
store.latitude = 39.413781
store.longitude = -77.422826
store.phone = '301-401-8202'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Gritty Goblin Games')
business.website = 'www.grittygoblingames.com'
business.facebook = 'www.facebook.com/grittygoblingames'
business.email = 'info@grittygoblingames.com'
business.save()

store = Store(business=business, city='Fulton', state_code='MD', zip_code='20759')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '8180 Maple Lawn Blvd'
store.address2 = 'Suite E'
store.latitude = 39.148120
store.longitude = -76.906923
store.phone = '240-360-5998'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Beyond Comics')
business.website = 'www.beyondcomics.com'
business.facebook = 'www.facebook.com/Beyond-Comics-69532697333'
business.save()

store = Store(business=business, city='Gaithersburg', state_code='MD', zip_code='20879')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '18749 N Frederick Ave'
store.latitude = 39.163650
store.longitude = -77.225354
store.phone = '301-216-0007'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Neverland Games - Lost Boys Hideout')
business.website = 'neverlandgames.tcgplayerpro.com'
business.facebook = 'www.facebook.com/Neverland.Games'
business.email = 'info@neverlandgamestore.com'
business.save()

store = Store(business=business, city='Hagerstown', state_code='MD', zip_code='21740')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '17301 Valley Mall Rd'
store.address2 = 'Suite 416'
store.latitude = 39.624662
store.longitude = -77.767881
store.phone = '240-513-6055'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Our House Games, LLC.')
business.website = 'www.ourhousegames.com'
business.facebook = 'www.facebook.com/OurHouseGames'
business.email = 'contact@ourhousegames.com'
business.save()

store = Store(business=business, city='Monroe', state_code='MI', zip_code='48161')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '1211 S Monroe St'
store.latitude = 41.905184
store.longitude = -83.406853
store.phone = '734-242-4263'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Dream Wizards')
business.website = 'www.dreamwizards.com'
business.facebook = 'www.facebook.com/dreamwizards'
business.email = 'sales@dreamwizards.com'
business.save()

store = Store(business=business, city='Rockville', state_code='MD', zip_code='20852')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '11772 Parklawn Dr'
store.latitude = 39.048085
store.longitude = -77.102418
store.phone = '301-881-3530'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Dice City Games')
business.facebook = 'www.facebook.com/dicecity'
business.save()

store = Store(business=business, city='Silver Spring', state_code='MD', zip_code='20902')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '11406-b Georgia Ave'
store.latitude = 39.041876
store.longitude = -77.052743
store.phone = '443-424-2637'.replace('-', '')
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Retrofix Games')
business.website = 'www.retrofixgames.com'
business.facebook = 'www.facebook.com/retrofixmissoula'
business.email = 'contact@retrofixgames.com'
business.save()

store = Store(business=business, city='Missoula', state_code='MT', zip_code='59801')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '1118 W Central Ave'
store.latitude = 46.851084
store.longitude = -114.015993
store.phone = '406-926-6911'.replace('-', '')
store.save()
