import django
import os

django.setup()

from apps.finder.models import Category
from apps.finder.models import Business

Category.objects.all().delete()
Business.objects.all().delete()

board_game_category = Category.objects.create(name='Board Games')
comics_category = Category.objects.create(name='Comics')

os.system('python us/a.py')
os.system('python us/c.py')
os.system('python us/d.py')
os.system('python us/i.py')
os.system('python us/k.py')
os.system('python us/m.py')
os.system('python us/n.py')
os.system('python us/o.py')
os.system('python us/s.py')
os.system('python us/t.py')
os.system('python us/u.py')
os.system('python us/v.py')
