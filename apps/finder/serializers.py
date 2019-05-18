from django.contrib.auth.models import User
from rest_framework import serializers

from apps.finder.models import Business
from apps.finder.models import BusinessLogItem
from apps.finder.models import Store
from apps.finder.models import StoreLogItem
from apps.finder.models import Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Tag
        fields = ('id',
                  'name',
                  'description')


class StoreLogItemSerializer(serializers.ModelSerializer):
    logItemType = serializers.IntegerField(source='log_item_type')
    user = UserSerializer()
    lastUpdated = serializers.DateTimeField(source='last_updated', format='iso-8601')

    class Meta:
        model = StoreLogItem
        fields = ('logItemType',
                  'user',
                  'lastUpdated')


class StoreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    address1 = serializers.CharField()
    address2 = serializers.CharField()
    city = serializers.CharField()
    stateCode = serializers.CharField(source='state_code')
    zipCode = serializers.CharField(source='zip_code')
    lat = serializers.DecimalField(source='latitude', max_digits=11, decimal_places=9)
    lng = serializers.DecimalField(source='longitude', max_digits=12, decimal_places=9)
    phone = serializers.CharField()
    logItems = StoreLogItemSerializer(source='log_items', many=True)

    class Meta:
        model = Store
        fields = ('id',
                  'name',
                  'address1',
                  'address2',
                  'city',
                  'stateCode',
                  'zipCode',
                  'lat',
                  'lng',
                  'phone',
                  'logItems')


class BusinessLogItemSerializer(serializers.ModelSerializer):
    logItemType = serializers.IntegerField(source='log_item_type')
    user = UserSerializer()
    lastUpdated = serializers.DateTimeField(source='last_updated', format='iso-8601')

    class Meta:
        model = BusinessLogItem
        fields = ('logItemType',
                  'user',
                  'lastUpdated')


class BusinessSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    website = serializers.CharField()
    email = serializers.CharField()
    facebook = serializers.CharField()
    stores = StoreSerializer(many=True, read_only=True)
    logItems = BusinessLogItemSerializer(source='log_items', many=True)

    class Meta:
        model = Business
        fields = ('id',
                  'name',
                  'website',
                  'email',
                  'facebook',
                  'stores',
                  'logItems')
