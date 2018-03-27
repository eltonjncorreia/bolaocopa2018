# Generated by Django 2.0.3 on 2018-03-27 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20180326_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aposta',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
