# Generated by Django 4.2.6 on 2023-11-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0007_alter_myuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.URLField(),
        ),
    ]