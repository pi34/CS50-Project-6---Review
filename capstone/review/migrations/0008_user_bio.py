# Generated by Django 3.1.2 on 2021-03-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_auto_20210302_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
