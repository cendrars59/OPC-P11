# Generated by Django 3.0.7 on 2020-07-08 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_userproductssearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproductssearch',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='user',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
