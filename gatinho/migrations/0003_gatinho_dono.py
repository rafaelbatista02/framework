# Generated by Django 3.0.2 on 2020-01-10 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dono', '0001_initial'),
        ('gatinho', '0002_gatinho_cor'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatinho',
            name='dono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dono.Dono'),
        ),
    ]
