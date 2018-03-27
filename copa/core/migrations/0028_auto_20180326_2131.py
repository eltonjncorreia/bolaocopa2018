# Generated by Django 2.0.3 on 2018-03-27 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20180326_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aposta',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
