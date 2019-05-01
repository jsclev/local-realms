import csv
import django

django.setup()

from apps.finder.models import ZipCode


ZipCode.objects.all().delete()
zip_codes = []

with open('./data/us_zip_codes.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        zip_code = ZipCode()
        zip_code.zip_code = row[1]
        zip_code.city = row[2]
        zip_code.state_name = row[3]
        zip_code.state_code = row[4]

        zip_codes.append(zip_code)

ZipCode.objects.bulk_create(zip_codes)

zip_codes = ZipCode.objects.all().order_by('state_code', 'city')
print('Total zip codes added to db: ' + str(zip_codes.count()))
