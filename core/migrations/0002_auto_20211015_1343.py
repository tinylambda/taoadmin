# Generated by Django 3.2.8 on 2021-10-15 13:43

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attr',
            name='dtype',
            field=models.CharField(choices=[('INT', 'Integer'), ('FLOAT', 'Float'), ('STRING', 'String')], default='STRING', max_length=64, verbose_name='Attr data type'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='hint',
            field=models.JSONField(blank=True, default=core.models.default_attr_hint, verbose_name='Attr hint'),
        ),
        migrations.AlterField(
            model_name='class',
            name='hint',
            field=models.JSONField(blank=True, default=core.models.default_class_hint, verbose_name='Class hint'),
        ),
    ]
