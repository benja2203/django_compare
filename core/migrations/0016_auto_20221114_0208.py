# Generated by Django 3.1.8 on 2022-11-14 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20221114_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('P1', 'Ropa1'), ('P2', 'Ropa2'), ('P3', 'Elec1'), ('P4', 'Elec2')], max_length=2),
        ),
    ]
