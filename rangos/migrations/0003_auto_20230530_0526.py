# Generated by Django 3.1.3 on 2023-05-30 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rangos', '0002_auto_20230530_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rango',
            name='posted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
