# Generated by Django 2.0.7 on 2018-07-20 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0028_spacebucks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doors',
            field=models.ManyToManyField(blank=True, to='portal.Doors'),
        ),
        migrations.AlterField(
            model_name='spacebucks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
