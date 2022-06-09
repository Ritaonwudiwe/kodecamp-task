# Generated by Django 4.0.4 on 2022-06-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_brand_product_p_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='p_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_column='p_name', max_length=10000),
        ),
    ]