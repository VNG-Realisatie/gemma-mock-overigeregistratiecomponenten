# Generated by Django 2.0.6 on 2019-01-15 11:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOfDienst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='uuid')),
                ('naam', models.CharField(max_length=80, verbose_name='naam')),
                ('omschrijving', models.TextField(blank=True, verbose_name='omschrijving')),
                ('webpagina', models.URLField(blank=True, verbose_name='webpagina')),
            ],
            options={
                'verbose_name': 'product of dienst',
                'verbose_name_plural': 'producten en diensten',
            },
        ),
    ]
