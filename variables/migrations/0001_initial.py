# Generated by Django 5.0.6 on 2024-06-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_name', models.CharField(max_length=255)),
                ('variable_type', models.CharField(choices=[('Input', 'Input'), ('Calculated', 'Calculated')], max_length=10)),
                ('variable_options', models.TextField(blank=True, null=True)),
                ('variable_definition', models.TextField(blank=True, null=True)),
                ('level_in_2023', models.FloatField()),
                ('units', models.CharField(blank=True, max_length=50, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('determining_value', models.CharField(blank=True, max_length=255, null=True)),
                ('multiplier', models.FloatField(blank=True, null=True)),
                ('standard_deviation_of_multiplier', models.FloatField(blank=True, null=True)),
                ('constant', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
