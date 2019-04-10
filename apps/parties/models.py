from django.db import models


class Organization(models.Model):
    name = models.TextField(null=True)

    class Meta:
        app_label = 'parties'
        db_table = 'organization'
