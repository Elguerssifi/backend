# Generated by Django 4.1.3 on 2023-01-01 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_message_historique'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message_historique',
            old_name='conversationi',
            new_name='historiquei',
        ),
    ]
