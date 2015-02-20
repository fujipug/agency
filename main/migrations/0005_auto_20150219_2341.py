# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150219_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='description',
            field=models.TextField(default=b'Description here'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='picture',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='freestuff',
            name='gift',
            field=models.CharField(max_length=10, choices=[(b'T-shirt', b'T-shirt'), (b'Sticker', b'Sticker'), (b'Keychain', b'Keychain')]),
            preserve_default=True,
        ),
    ]
