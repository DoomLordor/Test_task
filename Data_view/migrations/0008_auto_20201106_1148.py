# Generated by Django 3.1.2 on 2020-11-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_view', '0007_auto_20201106_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industryspecifictyping',
            name='name',
            field=models.TextField(verbose_name='Отраслевая типизация'),
        ),
        migrations.AlterField(
            model_name='statusegrul',
            name='name',
            field=models.TextField(verbose_name='Статус ЕГРЮЛ'),
        ),
        migrations.AlterField(
            model_name='statusrybpnybp',
            name='name',
            field=models.TextField(verbose_name='Статус РУБПНУБП'),
        ),
    ]
