# Generated by Django 4.0.4 on 2022-05-19 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_bjpvote_delete_bjpvotes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BjpVote',
        ),
        migrations.DeleteModel(
            name='SaralBooth',
        ),
    ]