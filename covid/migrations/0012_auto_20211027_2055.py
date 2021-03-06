# Generated by Django 3.2.8 on 2021-10-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0011_auto_20211027_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(3, 'other'), (2, 'K'), (1, 'M')]),
        ),
        migrations.AlterField(
            model_name='persons',
            name='hospitalization',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Nie'), (1, 'Tak')], default=0),
        ),
        migrations.AlterField(
            model_name='persons',
            name='quarantine',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Nie'), (1, 'Tak')], default=0),
        ),
        migrations.AlterField(
            model_name='persons',
            name='supervision',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Nie'), (1, 'Tak')], default=0),
        ),
    ]
