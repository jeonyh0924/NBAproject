# Generated by Django 2.1.5 on 2019-08-12 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signatureteam',
            name='player',
        ),
        migrations.RemoveField(
            model_name='signatureteam',
            name='user',
        ),
        migrations.DeleteModel(
            name='SignatureTeam',
        ),
    ]
