# Generated by Django 4.0.4 on 2022-05-05 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Titre', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titre',
            old_name='titre',
            new_name='nom',
        ),
    ]
