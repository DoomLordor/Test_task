# Generated by Django 3.1.2 on 2020-10-30 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data_view', '0004_auto_20201030_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='industry_specific_typing',
            new_name='id_industry_specific_typing',
        ),
    ]