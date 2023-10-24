# Generated by Django 4.2.6 on 2023-10-19 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_destinos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinos',
            name='Id',
            field=models.CharField(max_length=20, verbose_name='ID de Destino'),
        ),
        migrations.AlterField(
            model_name='destinos',
            name='activo',
            field=models.BooleanField(verbose_name='Estado (activo/inactivo)'),
        ),
        migrations.AlterField(
            model_name='destinos',
            name='city',
            field=models.CharField(max_length=20, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='destinos',
            name='country',
            field=models.CharField(max_length=100, verbose_name='Pais'),
        ),
        migrations.AlterField(
            model_name='destinos',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='destinos',
            name='tipo',
            field=models.BooleanField(verbose_name='Tipo (elegidos/recomendados)'),
        ),
        migrations.AlterField(
            model_name='destinos',
            name='urlImg',
            field=models.ImageField(null=True, upload_to='static/core/images/locations-img/', verbose_name='Destinos'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]