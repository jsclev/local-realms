import django
import os

django.setup()

from apps.finder.models import Category
from apps.finder.models import Business

Category.objects.all().delete()
Business.objects.all().delete()

board_game_category = Category.objects.create(name='Board Games')
comics_category = Category.objects.create(name='Comics')

os.system('python us/id.py')
os.system('python us/il.py')
os.system('python us/ks.py')
os.system('python us/md.py')
os.system('python us/nc.py')
os.system('python us/oh.py')
os.system('python us/sc.py')
os.system('python us/tn.py')
os.system('python us/ut.py')
os.system('python us/va.py')
os.system('python us/vt.py')
