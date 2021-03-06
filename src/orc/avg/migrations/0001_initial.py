# Generated by Django 2.0.6 on 2018-08-17 13:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InzageVerzoek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('inzage_wmo', models.BooleanField(help_text='Indicatie Inzage WMO')),
                ('inzage_jeugd', models.BooleanField(help_text='Indicatie Inzage Jeugd')),
                ('inzage_participatie', models.BooleanField(help_text='Indicatie Inzage Participatie')),
                ('inzage_veiligheidskamer', models.BooleanField(help_text='Indicatie Inzage Veiligheidskamer')),
                ('inzage_schuldhulpverlening', models.BooleanField(help_text='Indicatie Inzage Schuldhulpverlening')),
                ('inzage_overige_regelingen', models.BooleanField(help_text='Indicatie Inzage Overige regelingen')),
                ('onderwerp_overige_regelingen', models.CharField(blank=True, help_text='Onderwerp bij Overige Regelingen', max_length=200)),
                ('inzage_algemeen', models.BooleanField(help_text='Indicatie Inzage Algemeen')),
                ('reden_inzage_algemeen', models.CharField(blank=True, help_text='Reden Algemeen', max_length=200)),
                ('antwoord_per_email', models.BooleanField(help_text='Indicatie Antwoord per e-mail')),
            ],
            options={
                'verbose_name': 'domein specfiek',
                'verbose_name_plural': 'domein specfieken',
            },
        ),
    ]
