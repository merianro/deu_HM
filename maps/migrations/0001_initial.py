# Generated by Django 4.2.3 on 2023-08-08 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Cultivo', 'Cultivo'), ('Terreno', 'Terreno'), ('Rio', 'Rio')], max_length=25, null=True)),
                ('nombre', models.TextField()),
                ('address', models.TextField()),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('titulo', models.TextField()),
                ('texto', models.TextField()),
                ('nroVisita', models.AutoField(primary_key=True, serialize=False)),
                ('fechaHora', models.DateTimeField(auto_now_add=True)),
                ('entrevista', models.BooleanField(default=False)),
                ('fechaEntr', models.DateField(blank=True, null=True)),
                ('imagen', models.ImageField(upload_to='fotos/')),
                ('ubic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.address')),
                ('user', models.ForeignKey(default=users.models.CustomUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entrevistado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('edad', models.TextField()),
                ('profesion', models.TextField()),
                ('nota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entrevistados', to='maps.note')),
            ],
        ),
    ]
