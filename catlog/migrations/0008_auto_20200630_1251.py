# Generated by Django 3.0.7 on 2020-06-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0007_auto_20200630_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='code',
            field=models.CharField(max_length=1024, unique=True),
        ),
    ]
