# Generated by Django 2.0.3 on 2018-03-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180323_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='horario',
            field=models.DateField(),
        ),
    ]
