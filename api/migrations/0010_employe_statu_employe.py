# Generated by Django 4.1.3 on 2022-12-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_employe_image_employe'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='statu_employe',
            field=models.BooleanField(default=True),
        ),
    ]