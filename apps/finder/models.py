from django.db import models


class Category(models.Model):
    name = models.TextField(null=True)

    class Meta:
        db_table = 'category'


class Business(models.Model):
    name = models.TextField(null=True)
    website = models.TextField(null=True)
    yelp = models.TextField(null=True)
    youtube = models.TextField(null=True)
    facebook = models.TextField(null=True)
    twitter = models.TextField(null=True)
    email = models.TextField(null=True)

    class Meta:
        db_table = 'business'


class Store(models.Model):
    business = models.ForeignKey(Business, related_name='stores', on_delete=models.CASCADE)
    name = models.TextField(null=True)
    street1 = models.CharField(max_length=100, null=True)
    street2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state_code = models.CharField(max_length=2, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=9, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True)

    class Meta:
        db_table = 'store'


class CategoryQuantity(models.Model):
    business = models.ForeignKey(Business, related_name='category_quantities', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
