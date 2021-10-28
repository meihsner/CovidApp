# Generated by Django 3.2.8 on 2021-10-28 12:27

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0012_auto_20211027_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'M'), (2, 'K'), (3, 'other')])),
                ('age', models.PositiveSmallIntegerField()),
                ('telephone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date_of_received_information', models.DateField(blank=True, null=True)),
                ('date_of_positive_result', models.DateField(blank=True, null=True)),
                ('source_of_infection', models.TextField(blank=True, null=True)),
                ('hospitalization', models.PositiveSmallIntegerField(choices=[(0, 'Nie'), (1, 'Tak')], default=0)),
                ('supervision', models.PositiveSmallIntegerField(choices=[(0, 'Nie'), (1, 'Tak')], default=0)),
                ('quarantine', models.PositiveSmallIntegerField(choices=[(0, 'Nie'), (1, 'Tak')], default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Cities',
            new_name='City',
        ),
        migrations.RenameModel(
            old_name='Hospitals',
            new_name='Hospital',
        ),
        migrations.RenameModel(
            old_name='Laboratories',
            new_name='Laboratory',
        ),
        migrations.DeleteModel(
            name='Persons',
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='city', to='covid.city'),
        ),
        migrations.AddField(
            model_name='person',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hospital', to='covid.hospital'),
        ),
        migrations.AddField(
            model_name='person',
            name='laboratory_performing_tests',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='laboratory', to='covid.laboratory'),
        ),
        migrations.AddField(
            model_name='person',
            name='whereabouts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='whereabouts', to='covid.city'),
        ),
    ]
