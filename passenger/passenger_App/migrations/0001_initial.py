# Generated by Django 5.0.2 on 2024-03-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('passenger_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveBigIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('mobile_number', models.CharField(max_length=100)),
                ('travelPoints', models.IntegerField(max_length=10)),
            ],
        ),
    ]