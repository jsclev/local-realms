import csv
import django

django.setup()

from apps.finder.models import ZipCode


ZipCode.objects.all().delete()

with open('/Users/jcleveland/US.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        zip_code = ZipCode()
        zip_code.zip_code = row[1]
        zip_code.city = row[2]
        zip_code.state_name = row[3]
        zip_code.state_code = row[4]

        zip_code.save()

zip_codes = ZipCode.objects.all().order_by('state_code', 'city')

print('Total zip codes added to db: ' + str(zip_codes.count()))
