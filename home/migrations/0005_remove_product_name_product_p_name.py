# Generated by Django 4.0.4 on 2022-06-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_p_name_product_name_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='p_name',
            field=models.CharField(default='car', max_length=10000),
        ),
    ]