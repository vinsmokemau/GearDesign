# Generated by Django 2.2.1 on 2019-06-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0003_auto_20190531_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='Np',
            field=models.FloatField(choices=[(12, 12), (18, 18), (32, 32)], null=True, verbose_name='dientes del piñón'),
        ),
    ]