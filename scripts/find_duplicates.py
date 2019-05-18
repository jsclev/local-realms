import django

django.setup()

from apps.finder.models import Store

stores = Store.objects.all().order_by('business__name')

for store in stores:
    other_stores = Store.objects.filter(address1=store.address1,
                                        address2=store.address2,
                                        city=store.city,
                                        state_code=store.state_code).exclude(id=store.id)

    if other_stores.count() > 0:
        print('Found duplicate on ' + store.business.name)
