# Generated by Django 4.2.3 on 2023-07-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='notas',
            field=models.ManyToManyField(blank=True, to='maps.note'),
        ),
    ]
