from django.db import models


# class Party(models.Model):
#
#     class Meta:
#         db_table = 'party'


class Person(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1, null=True)
    birthdate = models.DateTimeField()

    class Meta:
        db_table = 'person'


class EmailAddress(models.Model):
    email_address = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'email_address'


class PhoneNumber(models.Model):
    # party = models.ForeignKey(Party, related_name='phone_numbers', on_delete=models.CASCADE)
    area_code = models.CharField(max_length=3, null=True)
    phone_number = models.CharField(max_length=7, null=True)
    # phone_number_type = models.ForeignKey(PhoneNumberType, on_delete=models.PROTECT, null=True)
    priority = models.IntegerField()

    class Meta:
        db_table = 'phone_number'


class Organization(models.Model):
    name = models.TextField(null=True)

    class Meta:
        db_table = 'organization'


class PostalAddress(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    street1 = models.CharField(max_length=100, null=True)
    street2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state_code = models.CharField(max_length=2, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=9, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True)

    class Meta:
        db_table = 'postal_address'
