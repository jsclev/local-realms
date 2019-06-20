from apps.accounts.util import check_is_admin
from apps.finder.models import Business
from apps.finder.models import Store, UserStoreSuggestion
from django.shortcuts import render
import settings


def maintenance(request):
    check_is_admin(request.user)
    return render(request, 'maintenance.html', locals())


def view_user_suggestions(request):
    check_is_admin(request.user)
    if request.method == "POST":
        post_values = request.POST

        name = post_values['name']
        address1 = post_values['address']
        address2 = post_values['address-line-2']
        city = post_values['city']
        state_code = post_values['state-code']
        zip_code = post_values['zip-code']
        latitude = post_values['latitude']
        longitude = post_values['longitude']
        phone = post_values['phone']
        website = post_values['website']
        facebook = post_values['facebook']
        email = post_values['email']

        if address2 is None:
            address2 = ''

        else:
            suggestion = UserStoreSuggestion.objects.get(id=post_values['id'])

            business = Business()
            business.name = name
            business.website = website
            business.facebook = facebook
            business.save()

            store = Store()
            store.user = suggestion.user
            store.business = business
            store.phone = phone
            store.address1 = address1
            store.address2 = address2
            store.city = city
            store.state_code = state_code
            store.zip_code = zip_code
            store.latitude = latitude
            store.longitude = longitude
            store.save()

            suggestion.is_verified = True
            suggestion.save()
    new_suggestions = UserStoreSuggestion.objects.filter(is_verified=False)
    return render(request, 'view_user_suggestions.html', locals())


def get_no_phone_stores(request):
    check_is_admin(request.user)
    version = settings.__version__

    businesses_with_no_website = Business.objects.filter(website='')
    num_businesses_with_no_website = businesses_with_no_website.count()

    stores_with_no_phone = Store.objects.filter(phone='')
    num_stores_with_no_phone = stores_with_no_phone.count()

    return render(request, 'view_incomplete.html', locals())
