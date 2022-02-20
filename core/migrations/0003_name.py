# Generated by Django 3.2.5 on 2021-10-03 13:35

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_delete_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.CharField(default=core.models.gen_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]