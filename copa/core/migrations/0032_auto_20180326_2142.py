# Generated by Django 2.0.3 on 2018-03-27 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20180326_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aposta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
