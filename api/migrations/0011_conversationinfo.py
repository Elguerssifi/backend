# Generated by Django 4.1.3 on 2022-12-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_employe_statu_employe'),
    ]

    operations = [
        migrations.CreateModel(
            name='conversationinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversationId', models.CharField(max_length=200)),
                ('pseudo_employe', models.CharField(default=None, max_length=200)),
                ('pseudo', models.CharField(default=None, max_length=200)),
            ],
        ),
    ]