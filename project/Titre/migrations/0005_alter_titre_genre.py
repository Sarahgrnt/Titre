# Generated by Django 4.0.4 on 2022-05-06 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Titre', '0004_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titre',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Titre.genre'),
        ),
    ]