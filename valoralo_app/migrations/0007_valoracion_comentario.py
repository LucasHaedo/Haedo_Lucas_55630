# Generated by Django 4.2.3 on 2023-08-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valoralo_app', '0006_consulta_producto_id_alter_consulta_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='valoracion',
            name='comentario',
            field=models.TextField(default=5),
            preserve_default=False,
        ),
    ]
