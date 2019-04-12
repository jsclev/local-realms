import django

django.setup()

from apps.finder.models import Category
from apps.finder.models import CategoryQuantity
from apps.finder.models import Business
from apps.finder.models import Store

Category.objects.all().delete()
Business.objects.all().delete()

board_game_category = Category.objects.create(name='Board Games')
comics_category = Category.objects.create(name='Comics')

business = Business(name='All About Games')
business.website = 'https://allaboutgames.com/'
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

business = Business(name='Asgards Gate')
business.website = 'https://asgardsgate.website'
business.facebook = 'https://www.facebook.com/asgardsgateholton'
business.save()

store = Store(business=business, state_code='KS')
store.street1 = '106 W 5th St'
store.street2 = None
store.city = 'Holton'
store.zip_code = '66436'
store.latitude = 39.465175
store.longitude = -95.735196
store.save()

business = Business.objects.create(name='Your Local Game Store')
store = Store(business=business, state_code='NC')
store.street1 = '6908 Matthews-Mint Hill Rd'
store.street2 = 'Suite 350'
store.city = 'Mint Hill'
store.zip_code = '28227'
store.latitude = 35.171643
store.longitude = -80.657079
store.save()

business = Business.objects.create(name='Hillside Games and Comics')
store = Store(business=business, state_code='NC')
store.street1 = '800 Fairview Rd'
store.street2 = 'Suite EE'
store.city = 'Asheville'
store.zip_code = '28803'
store.latitude = 35.570199
store.longitude = -82.507587
store.save()

business = Business.objects.create(name='Carolina Tabletop Games')
store = Store(business=business, state_code='NC')
store.street1 = '315 Main St'
store.street2 = '#1'
store.city = 'Pineville'
store.zip_code = '28134'
store.latitude = 35.085479
store.longitude = -80.890651
store.save()

business = Business.objects.create(name='Spandex City')
store = Store(business=business, state_code='NC')
store.street1 = '2914 Mt Holly-Huntersville Rd'
store.street2 = None
store.city = 'Charlotte'
store.zip_code = '28214'
store.latitude = 35.319121
store.longitude = -80.952932
store.save()

business = Business.objects.create(name="The Wyvern's Tale")
store = Store(business=business, state_code='NC')
store.street1 = '347 Merrimon Ave'
store.street2 = None
store.city = 'Asheville'
store.zip_code = '28801'
store.latitude = 35.610936
store.longitude = -82.554662
store.save()

business = Business.objects.create(name='The Deck Box')
store = Store(business=business, state_code='NC')
store.street1 = '3049 Hendersonville Rd'
store.street2 = 'Suite 30'
store.city = 'Fletcher'
store.zip_code = '28732'
store.latitude = 35.439584
store.longitude = -82.504974
store.save()

business = Business.objects.create(name='Frogtown Hobbies')
store = Store(business=business, state_code='OH')
store.street1 = '27250 Crossroad Parkway a'
store.street2 = None
store.city = 'Rossford'
store.zip_code = '43460'
store.latitude = 41.546179
store.longitude = -83.582045
store.save()

business = Business(name='Dark Mountain Games')
business.website = 'http://www.darkmountaingames.com'
business.email = 'darkmtngames@vermontel.net'
business.save()

store = Store(business=business, state_code='VT')
store.street1 = '27 Main St'
store.city = 'Springfield'
store.zip_code = '05156'
store.latitude = 43.299009
store.longitude = -72.482226
store.save()

