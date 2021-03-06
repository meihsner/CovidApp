# Generated by Django 3.2.8 on 2021-11-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0016_auto_20211102_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Kobieta'), (1, 'Mężczyzna'), (3, 'inna')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='hospitalization',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tak'), (0, 'Nie')], default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='quarantine',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tak'), (0, 'Nie')], default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='supervision',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tak'), (0, 'Nie')], default=0),
        ),
    ]
