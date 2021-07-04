# Generated by Django 3.2.4 on 2021-07-03 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coupon', '0002_auto_20210703_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='create_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
    ]
