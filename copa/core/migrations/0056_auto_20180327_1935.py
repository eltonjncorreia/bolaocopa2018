# Generated by Django 2.0.3 on 2018-03-27 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0055_auto_20180327_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aposta',
            name='user_aposta',
        ),
        migrations.AddField(
            model_name='aposta',
            name='user_da_aposta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_da_apostas', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]