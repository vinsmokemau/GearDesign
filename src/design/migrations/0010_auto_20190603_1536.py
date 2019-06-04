# Generated by Django 2.2.1 on 2019-06-03 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0009_auto_20190603_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='Yng',
            field=models.FloatField(null=True, verbose_name='Factor de fuerza por estres del engrane'),
        ),
        migrations.AddField(
            model_name='gear',
            name='Zng',
            field=models.FloatField(null=True, verbose_name='Factor de resistencia por picaduras del engrane'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Ynp',
            field=models.FloatField(null=True, verbose_name='Factor de fuerza por estres del piñón'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Znp',
            field=models.FloatField(null=True, verbose_name='Factor de resistencia por picaduras del piñón'),
        ),
    ]
