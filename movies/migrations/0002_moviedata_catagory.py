# Generated by Django 4.2.7 on 2023-11-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='catagory',
            field=models.CharField(default='action', max_length=200),
        ),
    ]