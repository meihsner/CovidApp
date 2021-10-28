# Generated by Django 3.2.8 on 2021-10-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0004_auto_20211027_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persons',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, 'M'), (2, 'K'), (3, 'other')]),
        ),
    ]
