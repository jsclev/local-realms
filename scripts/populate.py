import django
import os

django.setup()

from apps.finder.models import Category
from apps.finder.models import Business
from apps.finder.models import Tag

Tag.objects.all().delete()
Category.objects.all().delete()
Business.objects.all().delete()

board_game_category = Category.objects.create(name='Board Games')
comics_category = Category.objects.create(name='Comics')

Tag.objects.create(name='Tabletop Board Games')
Tag.objects.create(name='Card Games (CCGs and TCGs)')
Tag.objects.create(name='Miniatures')
Tag.objects.create(name='Role Playing Games')

Tag.objects.create(name='Warhammer Only')
Tag.objects.create(name='Play Space')
Tag.objects.create(name='Events and Tournaments')

# board games, comics, miniatures, RPGs and TCGs
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
