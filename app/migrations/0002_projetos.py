# Generated by Django 3.1.5 on 2021-02-03 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('url_hash', models.CharField(max_length=15, unique=True)),
                ('descricao', models.TextField()),
                ('privado', models.BooleanField(default=False)),
                ('encerrado', models.BooleanField(default=False)),
                ('administrador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='administrador', to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ManyToManyField(related_name='categorias_projeto', to='app.Categoria')),
                ('criador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criador', to=settings.AUTH_USER_MODEL)),
                ('moderador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moderador', to=settings.AUTH_USER_MODEL)),
                ('participantes', models.ManyToManyField(related_name='participantes_projeto', to=settings.AUTH_USER_MODEL)),
                ('pendentes', models.ManyToManyField(related_name='usuarios_pendentes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
