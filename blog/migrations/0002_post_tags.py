# Generated by Django 3.2 on 2021-06-10 17:40

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
       
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',

        ),
    ]
