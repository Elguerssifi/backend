# Generated by Django 4.1.3 on 2022-12-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_timing'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='payment',
            field=models.BooleanField(default=False),
        ),
    ]
