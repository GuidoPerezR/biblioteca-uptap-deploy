# Generated by Django 4.1.2 on 2022-11-09 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modulo', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrador',
            name='id_cargo',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='id_carrera',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='id_cuatrimestre',
        ),
        migrations.RemoveField(
            model_name='docente_administrativo',
            name='id_cargo',
        ),
        migrations.RemoveField(
            model_name='docente_administrativo',
            name='id_cuatrimestre',
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id_admin',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id_doc_ad',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='matricula',
        ),
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.DeleteModel(
            name='Carrera',
        ),
        migrations.DeleteModel(
            name='Cuatrimestre',
        ),
        migrations.DeleteModel(
            name='Docente_administrativo',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
