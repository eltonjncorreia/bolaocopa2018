# Generated by Django 2.0.3 on 2018-03-25 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_auto_20180323_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
