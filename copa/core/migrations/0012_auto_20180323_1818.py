# Generated by Django 2.0.3 on 2018-03-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20180323_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aposta',
            name='preco',
            field=models.CharField(blank=True, choices=[('2', '2'), ('5', '5'), ('10', '10'), ('20', '20')], max_length=1, null=True),
        ),
    ]
