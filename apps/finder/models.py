from django.db import models


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
    status = models.IntegerField(default=0, null=False)
    name = models.TextField(default='', blank=True)
    location_heading = models.TextField(default='')
    street1 = models.TextField(default='')
    street2 = models.TextField(default='')
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


class StoreLogItem(models.Model):
    store = models.ForeignKey(Store, related_name='log_items', on_delete=models.CASCADE)
    user = models.TextField(default=None)
    log_item_type = models.IntegerField(default=None, blank=True)
    timestamp = models.DateTimeField(default=None, blank=True)

    class Meta:
        db_table = 'store_log_item'


class ZipCode(models.Model):
    zip_code = models.TextField(default=None, blank=False)
    city = models.TextField(default=None, blank=False)
    state_name = models.TextField(default=None, blank=False)
    state_code = models.TextField(default=None, blank=False)

    class Meta:
        db_table = 'zip_code'
