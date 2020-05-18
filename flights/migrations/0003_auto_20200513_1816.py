# Generated by Django 3.0.6 on 2020-05-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight'),
        ),
    ]