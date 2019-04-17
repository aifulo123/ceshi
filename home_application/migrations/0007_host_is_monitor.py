# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0006_auto_20190417_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='is_monitor',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u76d1\u63a7'),
        ),
    ]
