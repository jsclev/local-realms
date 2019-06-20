import os
import django

django.setup()

from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model

from apps.finder.models import Category
from apps.finder.models import StoreBlacklistItem
from apps.finder.models import Tag

site = Site.objects.all()[0]
site.domain = 'localrealms.com'
site.name = 'Local Realms'
site.save()

user_model = get_user_model()
owner = user_model.objects.create_user('jsclev',
                                       password='john',
                                       email='john@localrealms.com',
                                       first_name='John',
                                       last_name='Cleveland',
                                       is_admin=True,
                                       is_owner=True)
admin = user_model.objects.create_user('admin',
                                       password='admin',
                                       email='admin@localrealms.com',
                                       first_name='Admin',
                                       last_name='Admin',
                                       is_admin=True,
                                       is_owner=False)

board_game_category = Category.objects.create(name='Board Games')
comics_category = Category.objects.create(name='Comics')

Tag.objects.create(name='Tabletop Board Games',
                   description='')
Tag.objects.create(name='CCGs, TCGs, and LCGs',
                   description="Magic, Poke'mon, Yu-Gi-Oh!, Netrunner, Star Wars, Game of Thrones")
Tag.objects.create(name='Miniature Games',
                   description='40K, Warhammer, Warmachine, X-Wing, Battletech, Drop Fleet')
Tag.objects.create(name='Role Playing Games',
                   description='Dungeons & Dragons, Pathfinder, Shadowrun, Star Wars')
Tag.objects.create(name='Warhammer Only')
Tag.objects.create(name='Play Space')
Tag.objects.create(name='Events and Tournaments')

StoreBlacklistItem.objects.create(name='Gamestop')
StoreBlacklistItem.objects.create(name='GameStop')
StoreBlacklistItem.objects.create(name='Barnes & Noble')
StoreBlacklistItem.objects.create(name='Barnes & Noble Booksellers')

os.system('python us/a.py')
os.system('python us/c.py')
os.system('python us/d.py')
os.system('python us/f.py')
os.system('python us/g.py')
os.system('python us/i.py')
os.system('python us/k.py')
os.system('python us/m.py')
os.system('python us/n.py')
os.system('python us/o.py')
os.system('python us/s.py')
os.system('python us/t.py')
os.system('python us/u.py')
os.system('python us/v.py')
os.system('python us/w.py')
