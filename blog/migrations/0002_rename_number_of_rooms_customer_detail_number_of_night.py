# Generated by Django 4.0.4 on 2022-06-17 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_detail',
            old_name='number_of_rooms',
            new_name='number_of_night',
        ),
    ]
