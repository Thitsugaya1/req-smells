# Generated by Django 3.2.7 on 2022-03-29 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20220324_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalizisRsDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smell_codigo', models.CharField(default=' ', max_length=700)),
                ('version', models.CharField(default='1', max_length=200)),
                ('rs_codigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.requisitosistema')),
            ],
            options={
                'verbose_name': 'Analisis Descripcion RS',
            },
        ),
        migrations.CreateModel(
            name='AnalisisRuDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smell_codigo', models.CharField(default=' ', max_length=700)),
                ('version', models.CharField(default='1', max_length=200)),
                ('ru_codigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.requisitodeusuario')),
            ],
            options={
                'verbose_name': 'Analisis Descripcion RU',
            },
        ),
    ]
