# Generated by Django 4.2.3 on 2023-07-22 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_category',
            new_name='cat',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_description',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_sub_category',
            new_name='subcat',
        ),
    ]