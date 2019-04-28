from rest_framework import serializers

from apps.finder.models import Business
from apps.finder.models import Store
from apps.finder.models import Tag


class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Tag
        fields = ('id',
                  'name',
                  'description')


class StoreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    street1 = serializers.CharField()
    street2 = serializers.CharField()
    city = serializers.CharField()
    stateCode = serializers.CharField(source='state_code')
    zipCode = serializers.CharField(source='zip_code')
    lat = serializers.DecimalField(source='latitude', max_digits=11, decimal_places=9)
    lng = serializers.DecimalField(source='longitude', max_digits=12, decimal_places=9)
    phone = serializers.CharField()

    class Meta:
        model = Store
        fields = ('id',
                  'name',
                  'street1',
                  'street2',
                  'city',
                  'stateCode',
                  'zipCode',
                  'lat',
                  'lng',
                  'phone')


class BusinessSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    website = serializers.CharField()
    email = serializers.CharField()
    facebook = serializers.CharField()
    stores = StoreSerializer(many=True, read_only=True)

    class Meta:
        model = Business
        fields = ('id',
                  'name',
                  'website',
                  'email',
                  'facebook',
                  'stores')
