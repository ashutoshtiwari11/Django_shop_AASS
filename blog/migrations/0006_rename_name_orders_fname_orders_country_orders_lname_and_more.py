# Generated by Django 4.2.3 on 2023-07-26 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contactdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='orders',
            name='country',
            field=models.CharField(default='India', max_length=50),
        ),
        migrations.AddField(
            model_name='orders',
            name='lname',
            field=models.CharField(default=' ', max_length=90),
        ),
        migrations.AddField(
            model_name='orders',
            name='username',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
