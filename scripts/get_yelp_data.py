import django, json, httplib2, time
from json import loads

django.setup()

from apps.finder.models import Business, Store, ZipCode

http = httplib2.Http()

API_KEY = 'hXucEQ6lnOGgmAE6JW3YkMNs56tJGCLy4wpdS11KYqWtWpLCBOYNEi' \
          'Qn_J9ieiewQOqHGWSiqIF-GugcPwvOuBFPQ1hAEScUip_zKdcsgxsCm9OgrteFm_Lo96jHXHYx'

headers = {
    'Authorization': 'Bearer ' + API_KEY,
}

business_ids = set()

zip_codes = ZipCode.objects.filter(state_code='RI').order_by('state_code', 'zip_code')

for zip_code in zip_codes:
    print('Getting stores for ' + zip_code.zip_code)
    params = 'location=' + zip_code.zip_code
    params += '&'
    params += 'categories=tabletopgames'
    params += '&'
    params += 'radius=25000'
    url = 'https://api.yelp.com/v3/businesses/search?' + params

    time.sleep(.025)
    response, content = http.request(url, 'GET', headers=headers)

    json_obj = loads(content)

    if 'businesses' in json_obj:
        for json_business in json_obj['businesses']:
            business_ids.add(json_business['id'])
    else:
        print('Error on ' + str(json_obj))

with open('./data/yelp.json', 'a') as outfile:
    for business_id in business_ids:
        url = 'https://api.yelp.com/v3/businesses/' + business_id

        response, content = http.request(url, 'GET', headers=headers)

        json_obj = loads(content)

        name = json_obj['name']
        city = json_obj['location']['city']
        state_code = json_obj['location']['state']
        zip_code = json_obj['location']['zip_code']

        if Store.objects.filter(business__name=name,
                                city=city,
                                state_code=state_code,
                                zip_code=zip_code).exists():
            print('Store already exists: ' + str(json_obj))
        else:
            json.dump(json_obj, outfile, ensure_ascii=False)
            outfile.write('\n')
            # business = Business()
            # business.name = json_obj['name']
            # business.save()
            #
            # store = Store()
            # store.business = business
            # store.phone = json_obj['phone']
            # store.street1 = json_obj['location']['address1']
            # store.city = json_obj['location']['city']
            # store.state_code = json_obj['location']['state']
            # store.zip_code = json_obj['location']['zip_code']
            # store.latitude = json_obj['coordinates']['latitude']
            # store.longitude = json_obj['coordinates']['longitude']
            # store.save()
