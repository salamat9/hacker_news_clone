# Generated by Django 3.2.9 on 2021-11-09 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_up_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='up_votes',
            new_name='upvotes',
        ),
    ]