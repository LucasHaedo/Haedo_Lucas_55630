# Generated by Django 4.2.3 on 2023-08-27 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('valoralo_app', '0005_consulta_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='producto_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
