import django
from django.conf import settings

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Your Local Game Store')
business.website = 'www.yourlocalgamestore.com'
business.save()

store = Store(business=business, city='Mint Hill', state_code='NC', zip_code='28227')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '6908 Matthews-Mint Hill Rd'
store.address2 = 'Suite 350'
store.latitude = 35.171643
store.longitude = -80.657079
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Hillside Games and Comics')
business.website = 'hillsidegames.com'
business.save()

store = Store(business=business, city='Asheville', state_code='NC', zip_code='28803')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '800 Fairview Rd'
store.address2 = 'Suite EE'
store.latitude = 35.570199
store.longitude = -82.507587
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Carolina Tabletop Games')
business.facebook = 'www.facebook.com/carolinatabletopgames'
business.save()

store = Store(business=business, city='Pineville', state_code='NC', zip_code='28134')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '315 Main St'
store.address2 = '#1'
store.latitude = 35.085479
store.longitude = -80.890651
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='Spandex City')
business.website = 'spandexcity.com'
business.save()

store = Store(business=business, city='Charlotte', state_code='NC', zip_code='28214')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '2914 Mt Holly-Huntersville Rd'
store.latitude = 35.319121
store.longitude = -80.952932
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name="The Wyvern's Tale")
business.website = 'www.thewyvernstaleavl.com'
business.save()

store = Store(business=business, city='Asheville', state_code='NC', zip_code='28801')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '347 Merrimon Ave'
store.latitude = 35.610936
store.longitude = -82.554662
store.save()

###############################################################################
# Business
###############################################################################
business = Business.objects.create(name='The Deck Box')
business.website = 'www.thedeckbox.com'
business.save()

store = Store(business=business, city='Fletcher', state_code='NC', zip_code='28732')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.address1 = '3049 Hendersonville Rd'
store.address2 = 'Suite 30'
store.latitude = 35.439584
store.longitude = -82.504974
store.save()

###############################################################################
# Business
###############################################################################
business = Business(name='G2K Games')
business.website = 'www.g2kgames.net'
business.save()

store = Store(business=business, city='Morganton', state_code='NC', zip_code='28655')
store.status = settings.GLOBAL_CONSTANTS['STATUS_OPEN']
store.name = 'Morganton – Morganton Heights Shopping Center'
store.address1 = 'E150 Morganton Heights Blvd'
store.latitude = 35.725135
store.longitude = -81.704035
store.save()
