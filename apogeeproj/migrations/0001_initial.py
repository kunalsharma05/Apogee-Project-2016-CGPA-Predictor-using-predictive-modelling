# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_type', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'experiences',
            },
        ),
    ]