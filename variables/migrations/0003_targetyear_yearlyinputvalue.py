# Generated by Django 4.2.13 on 2024-06-27 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('variables', '0002_alter_variable_determining_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='YearlyInputValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('value', models.FloatField()),
                ('target_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearly_input_values', to='variables.targetyear')),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearly_input_values', to='variables.variable')),
            ],
            options={
                'unique_together': {('target_year', 'variable', 'year')},
            },
        ),
    ]
