# Generated by Django 4.2.13 on 2024-07-17 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('variables', '0007_alter_variable_interpolation_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variable',
            name='interpolation_method',
        ),
    ]