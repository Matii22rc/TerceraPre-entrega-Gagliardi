# Generated by Django 4.2.4 on 2023-08-28 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mati', '0002_rename_profesor_profesores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='camada',
            new_name='comision',
        ),
    ]