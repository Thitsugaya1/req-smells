# Generated by Django 3.2.7 on 2021-10-24 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211022_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionJefeProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.cuenta')),
                ('proyecto_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.proyecto')),
            ],
        ),
    ]
