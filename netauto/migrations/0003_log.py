# Generated by Django 3.0.3 on 2020-03-07 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netauto', '0002_auto_20200303_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=200)),
                ('action', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('messages', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(null=True)),
            ],
        ),
    ]
