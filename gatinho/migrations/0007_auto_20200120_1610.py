# Generated by Django 3.0.2 on 2020-01-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dono', '0001_initial'),
        ('gatinho', '0006_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_empresa', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('telefone', models.CharField(max_length=15)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gatinho',
            name='cor',
            field=models.CharField(choices=[('PRETO', 'Preto'), ('BRANCO', 'Branco'), ('LARANJA', 'Laranja'), ('CINZA', 'Cinza'), ('TRICOLOR', 'Tricolor'), ('BEGE', 'Bege')], max_length=100),
        ),
        migrations.AlterField(
            model_name='gatinho',
            name='dono',
            field=models.ManyToManyField(blank=True, to='dono.Dono'),
        ),
    ]
