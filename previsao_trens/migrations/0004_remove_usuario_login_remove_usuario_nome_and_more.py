# Generated by Django 5.0.2 on 2024-03-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('previsao_trens', '0003_usuario_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='login',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='sobrenome',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos_de_perfil'),
        ),
    ]
