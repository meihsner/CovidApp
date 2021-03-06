# Generated by Django 3.2.8 on 2021-10-27 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0007_auto_20211027_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='city', to='covid.cities'),
        ),
        migrations.AlterField(
            model_name='persons',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(2, 'K'), (1, 'M'), (3, 'other')]),
        ),
    ]
