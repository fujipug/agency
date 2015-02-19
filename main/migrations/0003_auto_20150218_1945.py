# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150218_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeStuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=256)),
                ('email', models.CharField(default=b'', max_length=256)),
                ('address', models.CharField(default=b'', max_length=256)),
                ('state', models.CharField(default=b'', max_length=2)),
                ('zipcode', models.CharField(default=b'', max_length=6)),
                ('gift', models.CharField(default=b'T-shirt', max_length=2, choices=[(b'T-shirt', b'T-shirt'), (b'Sticker', b'Sticker'), (b'Keychain', b'Keychain')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='PostForm',
        ),
    ]
