# Generated by Django 5.1.2 on 2024-10-29 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spotifytoken',
            old_name='expires_in',
            new_name='expires_at',
        ),
    ]
