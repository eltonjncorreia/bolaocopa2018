# Generated by Django 2.0.3 on 2018-03-27 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20180326_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aposta',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to=settings.AUTH_USER_MODEL),
        ),
    ]
