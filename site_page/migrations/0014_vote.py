# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-15 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_page', '0013_auto_20170115_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('give_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_page.Answer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_page.UserProfile')),
            ],
        ),
    ]
