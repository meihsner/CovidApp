# Generated by Django 3.2.8 on 2021-11-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0014_auto_20211101_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(3, 'other'), (1, 'M'), (2, 'K')]),
        ),
    ]