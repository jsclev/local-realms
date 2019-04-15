import django

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


business = Business.objects.create(name='Your Local Game Store')
business.website = 'www.yourlocalgamestore.com/'
business.save()

store = Store(business=business, state_code='NC')
store.street1 = '6908 Matthews-Mint Hill Rd'
store.street2 = 'Suite 350'
store.city = 'Mint Hill'
store.zip_code = '28227'
store.latitude = 35.171643
store.longitude = -80.657079
store.save()

business = Business.objects.create(name='Hillside Games and Comics')
business.website = 'hillsidegames.com'
business.save()

store = Store(business=business, state_code='NC')
store.street1 = '800 Fairview Rd'
store.street2 = 'Suite EE'
store.city = 'Asheville'
store.zip_code = '28803'
store.latitude = 35.570199
store.longitude = -82.507587
store.save()

business = Business.objects.create(name='Carolina Tabletop Games')
business.facebook = 'www.facebook.com/carolinatabletopgames'
business.save()

store = Store(business=business, state_code='NC')
store.street1 = '315 Main St'
store.street2 = '#1'
store.city = 'Pineville'
store.zip_code = '28134'
store.latitude = 35.085479
store.longitude = -80.890651
store.save()

business = Business.objects.create(name='Spandex City')
business.website = 'spandexcity.com'
business.save()

store = Store(business=business, state_code='NC')
store.street1 = '2914 Mt Holly-Huntersville Rd'
store.street2 = None
store.city = 'Charlotte'
store.zip_code = '28214'
store.latitude = 35.319121
store.longitude = -80.952932
store.save()

business = Business.objects.create(name="The Wyvern's Tale")
business.website = 'www.thewyvernstaleavl.com'
business.save()

store = Store(business=business, state_code='NC')
store.street1 = '347 Merrimon Ave'
store.street2 = None
store.city = 'Asheville'
store.zip_code = '28801'
store.latitude = 35.610936
store.longitude = -82.554662
store.save()

business = Business.objects.create(name='The Deck Box')
business.website = 'www.thedeckbox.com'
business.save()

store = Store(business=business, state_code='NC')
store.street1 = '3049 Hendersonville Rd'
store.street2 = 'Suite 30'
store.city = 'Fletcher'
store.zip_code = '28732'
store.latitude = 35.439584
store.longitude = -82.504974
store.save()

business = Business(name='G2K Games')
business.website = 'www.g2kgames.net'
business.save()

store = Store(business=business, state_code='NC')
store.name = 'Morganton – Morganton Heights Shopping Center'
store.street1 = 'E150 Morganton Heights Blvd'
store.city = 'Morganton'
store.zip_code = '28655'
store.latitude = 35.725135
store.longitude = -81.704035
store.save()
