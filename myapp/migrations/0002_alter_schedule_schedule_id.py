# Generated by Django 5.0.6 on 2024-06-09 13:40

import myapp.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='schedule_id',
            field=myapp.models.MultipleOfThreeField(primary_key=True, serialize=False),
        ),
    ]
