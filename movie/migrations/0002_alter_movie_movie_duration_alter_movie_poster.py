# Generated by Django 4.2.5 on 2023-10-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_duration',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='admin_page/static/img/'),
        ),
    ]
