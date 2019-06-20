from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    name = models.TextField(default=None, blank=False)

    class Meta:
        db_table = 'category'


class Tag(models.Model):
    name = models.TextField(default=None, blank=False)
    description = models.TextField(default='')

    class Meta:
        db_table = 'tag'


class Business(models.Model):
    name = models.TextField(default=None, blank=False)
    website = models.TextField(default='')
    yelp = models.TextField(default='')
    youtube = models.TextField(default='')
    facebook = models.TextField(default='')
    twitter = models.TextField(default='')
    email = models.TextField(default='')

    class Meta:
        db_table = 'business'


class Store(models.Model):
    business = models.ForeignKey(Business, related_name='stores', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, related_name='accepted_contributions', on_delete=models.SET_NULL)
    status = models.IntegerField(default=0, null=False)
    name = models.TextField(default='', blank=True)
    location_heading = models.TextField(default='')
    address1 = models.TextField(default='')
    address2 = models.TextField(default='')
    city = models.TextField(default='')
    state_code = models.CharField(max_length=2, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    phone = models.TextField(default='')
    latitude = models.DecimalField(max_digits=11, decimal_places=9, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True)
    website = models.TextField(default='')
    yelp = models.TextField(default='')
    youtube = models.TextField(default='')
    facebook = models.TextField(default='')
    twitter = models.TextField(default='')
    email = models.TextField(default='')

    class Meta:
        db_table = 'store'


class UserStoreSuggestion(models.Model):
    edit_store = models.ForeignKey(Store, null=True, related_name="edits", on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, related_name='suggested_contributions', on_delete=models.SET_NULL)
    is_verified = models.BooleanField(default=False)
    name = models.TextField(default='', blank=True)
    location_heading = models.TextField(default='')
    address1 = models.TextField(default='')
    address2 = models.TextField(default='')
    city = models.TextField(default='')
    state = models.CharField(max_length=2, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    phone = models.TextField(default='')
    latitude = models.DecimalField(max_digits=11, decimal_places=9, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True)
    website = models.TextField(default='')
    facebook = models.TextField(default='')
    email = models.TextField(default='')


class StoreBlacklistItem(models.Model):
    name = models.TextField(default='', blank=True)

    class Meta:
        db_table = 'store_blacklist_item'


class StoreTag(models.Model):
    store = models.ForeignKey(Business, related_name='tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'store_tag'


class CategoryQuantity(models.Model):
    business = models.ForeignKey(Business, related_name='category_quantities', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class BusinessLogItem(models.Model):
    business = models.ForeignKey(Business, related_name='log_items', on_delete=models.CASCADE)
    log_item_type = models.IntegerField(default=None, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=False)
    last_updated = models.DateTimeField(default=None, blank=True)

    class Meta:
        db_table = 'business_log_item'


class StoreLogItem(models.Model):
    store = models.ForeignKey(Store, related_name='log_items', on_delete=models.CASCADE)
    log_item_type = models.IntegerField(default=None, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=False)
    last_updated = models.DateTimeField(default=None, blank=True)

    class Meta:
        db_table = 'store_log_item'


class ZipCode(models.Model):
    zip_code = models.TextField(default=None, blank=False)
    city = models.TextField(default=None, blank=False)
    state_name = models.TextField(default=None, blank=False)
    state_code = models.TextField(default=None, blank=False)

    class Meta:
        db_table = 'zip_code'
