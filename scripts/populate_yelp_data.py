import django
import json

django.setup()

from apps.finder.models import Business
from apps.finder.models import Store


with open('./data/yelp.json', 'r') as f:
    for line in f:
        json_obj = json.loads(line)

        name = json_obj['name']
        address1 = json_obj['location']['address1']
        address2 = json_obj['location']['address2']
        city = json_obj['location']['city']
        state_code = json_obj['location']['state']
        zip_code = json_obj['location']['zip_code']
        latitude = json_obj['coordinates']['latitude']
        longitude = json_obj['coordinates']['longitude']

        if address2 is None:
            address2 = ''

        if Store.objects.filter(business__name=name,
                                city=city,
                                state_code=state_code,
                                zip_code=zip_code).exists():
            print('Store already exists: ' + str(json_obj))
        else:
            business = Business()
            business.name = name
            business.save()

            store = Store()
            store.business = business
            store.phone = json_obj['phone']
            store.address1 = address1
            store.address2 = address2
            store.city = city
            store.state_code = state_code
            store.zip_code = zip_code
            store.latitude = latitude
            store.longitude = longitude
            store.save()
