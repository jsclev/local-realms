import dateutil.parser
from django.contrib.auth.models import User

from apps.finder.models import BusinessLogItem
from apps.finder.models import StoreLogItem


def create_business_log_item(business, log_item_type, date_string):
    user = User.objects.get(username='jsclev')

    log_item = BusinessLogItem()
    log_item.business = business
    log_item.log_item_type = log_item_type
    log_item.user = user
    log_item.last_updated = dateutil.parser.parse(date_string)
    log_item.save()


def create_store_log_item(store, log_item_type, date_string):
    user = User.objects.get(username='jsclev')

    log_item = StoreLogItem()
    log_item.store = store
    log_item.log_item_type = log_item_type
    log_item.user = user
    log_item.last_updated = dateutil.parser.parse(date_string)
    log_item.save()
