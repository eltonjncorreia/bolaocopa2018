# Generated by Django 2.0.3 on 2018-03-28 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20180327_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selecao',
            name='bandeira',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
