# Generated by Django 3.1.2 on 2021-02-01 06:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20210124_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
