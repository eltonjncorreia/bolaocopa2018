# Generated by Django 2.0.3 on 2018-03-27 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_auto_20180327_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aposta',
            name='user_aposta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_apostas', to=settings.AUTH_USER_MODEL),
        ),
    ]
