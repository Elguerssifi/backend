# Generated by Django 4.1.3 on 2022-12-29 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_utilisateur_nbr_min'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='nbr_min',
            new_name='nbr_sc',
        ),
    ]
