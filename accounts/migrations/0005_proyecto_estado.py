# Generated by Django 3.1.7 on 2021-07-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210708_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
