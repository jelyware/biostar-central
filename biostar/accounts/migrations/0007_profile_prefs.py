# Generated by Django 2.2 on 2019-06-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='digest_prefs',
            field=models.IntegerField(choices=[(0, 'Never'), (1, 'Daily'), (2, 'Weekly'), (3, 'Monthly'), (4, 'Email for every new thread (mailing list mode)')], default=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='message_prefs',
            field=models.IntegerField(choices=[(3, 'Default'), (1, 'Email'), (0, 'Local Messages'), (2, 'No messages')], default=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.IntegerField(choices=[(0, 'Reader'), (1, 'Moderator'), (2, 'Admin'), (3, 'Blog User')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='text',
            field=models.TextField(blank=True, default='No profile information', max_length=10000, null=True),
        ),
    ]
