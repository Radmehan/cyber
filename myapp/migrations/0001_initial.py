# Generated by Django 5.0.6 on 2024-06-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
