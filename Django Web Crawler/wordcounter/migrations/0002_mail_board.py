# Generated by Django 3.1.6 on 2021-02-09 16:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcounter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='board',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8), blank=True, null=True, size=8),
        ),
    ]