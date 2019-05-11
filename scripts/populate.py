import django
import os

django.setup()

from apps.finder.models import Category
from apps.finder.models import Business
from apps.finder.models import StoreBlacklistItem
from apps.finder.models import Tag

Tag.objects.all().delete()
Category.objects.all().delete()
Business.objects.all().delete()

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
