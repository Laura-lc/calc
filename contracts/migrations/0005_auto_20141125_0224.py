# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_auto_20141125_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_end',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_start',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
