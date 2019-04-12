from rest_framework import serializers

from apps.finder.models import Organization
from apps.finder.models import PostalAddress


class PostalAddressSerializer(serializers.ModelSerializer):
    street1 = serializers.CharField()
    street2 = serializers.CharField()
    city = serializers.CharField()
    stateCode = serializers.CharField(source='state_code')
    zipCode = serializers.CharField(source='zip_code')
    lat = serializers.DecimalField(source='latitude', max_digits=11, decimal_places=9)
    lng = serializers.DecimalField(source='longitude', max_digits=12, decimal_places=9)

    class Meta:
        model = PostalAddress
        fields = ('street1',
                  'street2',
                  'city',
                  'stateCode',
                  'zipCode',
                  'lat',
                  'lng')


class OrganizationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    postalAddresses = PostalAddressSerializer(source='postal_addresses', many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('id',
                  'name',
                  'postalAddresses')
