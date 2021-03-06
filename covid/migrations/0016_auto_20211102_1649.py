# Generated by Django 3.2.8 on 2021-11-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0015_auto_20211101_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='who_added',
            field=models.CharField(default='None', max_length=32),
        ),
        migrations.AlterField(
            model_name='person',
            name='hospitalization',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Nie'), (1, 'Tak')], default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='quarantine',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Nie'), (1, 'Tak')], default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='supervision',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Nie'), (1, 'Tak')], default=0),
        ),
    ]
