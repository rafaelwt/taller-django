# Generated by Django 5.0.2 on 2024-02-14 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_alter_autordb_options_rename_autor_frasedb_autor_fk_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frasedb',
            options={'verbose_name': 'Frase', 'verbose_name_plural': 'Frases'},
        ),
        migrations.AlterModelTable(
            name='frasedb',
            table='Frases',
        ),
    ]
