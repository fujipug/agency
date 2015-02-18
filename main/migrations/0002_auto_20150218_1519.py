# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'')),
                ('party', models.CharField(default=b'', max_length=10)),
                ('description', models.TextField(default=b'Description missing.')),
                ('picture', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='postform',
            name='content',
        ),
        migrations.RemoveField(
            model_name='postform',
            name='created_at',
        ),
        migrations.AddField(
            model_name='postform',
            name='address',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postform',
            name='email',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postform',
            name='name',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postform',
            name='state',
            field=models.CharField(default=b'', max_length=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postform',
            name='zipcode',
            field=models.CharField(default=b'', max_length=6),
            preserve_default=True,
        ),
    ]
