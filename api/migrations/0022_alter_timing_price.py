# Generated by Django 4.1.3 on 2023-01-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_employe_nbr_utilisateurs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing',
            name='price',
            field=models.FloatField(max_length=100),
        ),
    ]
