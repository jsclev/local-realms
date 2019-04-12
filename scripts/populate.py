import django

django.setup()

from apps.finder.models import Category
from apps.finder.models import CategoryQuantity
from apps.finder.models import Organization
from apps.finder.models import PostalAddress

Category.objects.all().delete()
Organization.objects.all().delete()

board_game_category = Category.objects.create(name='Board Games')
comics_category = Category.objects.create(name='Comics')

org = Organization(name='Asgards Gate')
org.website = 'https://asgardsgate.website'
org.facebook = 'https://www.facebook.com/asgardsgateholton'
org.save()

pa = PostalAddress(organization=org, state_code='KS')
pa.street1 = '106 W 5th St'
pa.street2 = None
pa.city = 'Holton'
pa.zip_code = '66436'
pa.latitude = 39.465175
pa.longitude = -95.735196
pa.save()


org = Organization(name='Asgards Gate')
org.website = 'https://asgardsgate.website'
org.facebook = 'https://www.facebook.com/asgardsgateholton'
org.save()

pa = PostalAddress(organization=org, state_code='KS')
pa.street1 = '106 W 5th St'
pa.street2 = None
pa.city = 'Holton'
pa.zip_code = '66436'
pa.latitude = 39.465175
pa.longitude = -95.735196
pa.save()

org = Organization.objects.create(name='Your Local Game Store')
pa = PostalAddress(organization=org, state_code='NC')
pa.street1 = '6908 Matthews-Mint Hill Rd'
pa.street2 = 'Suite 350'
pa.city = 'Mint Hill'
pa.zip_code = '28227'
pa.latitude = 35.171643
pa.longitude = -80.657079
pa.save()

org = Organization.objects.create(name='Hillside Games and Comics')
pa = PostalAddress(organization=org, state_code='NC')
pa.street1 = '800 Fairview Rd'
pa.street2 = 'Suite EE'
pa.city = 'Asheville'
pa.zip_code = '28803'
pa.latitude = 35.570199
pa.longitude = -82.507587
pa.save()

org = Organization.objects.create(name='Carolina Tabletop Games')
pa = PostalAddress(organization=org, state_code='NC')
pa.street1 = '315 Main St'
pa.street2 = '#1'
pa.city = 'Pineville'
pa.zip_code = '28134'
pa.latitude = 35.085479
pa.longitude = -80.890651
pa.save()

org = Organization.objects.create(name='Spandex City')
pa = PostalAddress(organization=org, state_code='NC')
pa.street1 = '2914 Mt Holly-Huntersville Rd'
pa.street2 = None
pa.city = 'Charlotte'
pa.zip_code = '28214'
pa.latitude = 35.319121
pa.longitude = -80.952932
pa.save()

org = Organization.objects.create(name="The Wyvern's Tale")
pa = PostalAddress(organization=org, state_code='NC')
pa.street1 = '347 Merrimon Ave'
pa.street2 = None
pa.city = 'Asheville'
pa.zip_code = '28801'
pa.latitude = 35.610936
pa.longitude = -82.554662
pa.save()

org = Organization.objects.create(name='The Deck Box')
pa = PostalAddress(organization=org, state_code='NC')
pa.street1 = '3049 Hendersonville Rd'
pa.street2 = 'Suite 30'
pa.city = 'Fletcher'
pa.zip_code = '28732'
pa.latitude = 35.439584
pa.longitude = -82.504974
pa.save()

org = Organization.objects.create(name='Frogtown Hobbies')
pa = PostalAddress(organization=org, state_code='OH')
pa.street1 = '27250 Crossroad Parkway a'
pa.street2 = None
pa.city = 'Rossford'
pa.zip_code = '43460'
pa.latitude = 41.546179
pa.longitude = -83.582045
pa.save()

org = Organization(name='Dark Mountain Games')
org.website = 'http://www.darkmountaingames.com'
org.email = 'darkmtngames@vermontel.net'
org.save()

pa = PostalAddress(organization=org, state_code='VT')
pa.street1 = '27 Main St'
pa.city = 'Springfield'
pa.zip_code = '05156'
pa.latitude = 43.299009
pa.longitude = -72.482226
pa.save()

