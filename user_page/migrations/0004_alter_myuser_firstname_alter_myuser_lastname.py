# Generated by Django 4.2.6 on 2023-10-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0003_myuser_country_myuser_firstname_myuser_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='firstname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='lastname',
            field=models.CharField(max_length=100),
        ),
    ]
