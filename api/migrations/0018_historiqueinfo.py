# Generated by Django 4.1.3 on 2023-01-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_rename_nbr_min_utilisateur_nbr_sc'),
    ]

    operations = [
        migrations.CreateModel(
            name='historiqueinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historiqueId', models.CharField(max_length=200)),
                ('pseudo_employe', models.CharField(default=None, max_length=200)),
                ('pseudo', models.CharField(default=None, max_length=200)),
            ],
        ),
    ]