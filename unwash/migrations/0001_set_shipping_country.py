# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

from oscar.apps.address.models import Country


class Migration(DataMigration):
    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        info = (
            ('GB', False),
            ('US', True),
        )

        self.migrate(orm, info)

    def backwards(self, orm):
        "Write your backwards methods here."

        info = (
            ('GB', True),
            ('US', False),
        )

        self.migrate(orm, info)

    def migrate(self, orm, info):
        for country_id, is_shipping_country in info:
            country = Country.objects.get(iso_3166_1_a2=country_id)
            country.is_shipping_country = is_shipping_country

            country.save()

    models = {}

    complete_apps = ['address', 'unwash']
    symmetrical = True
