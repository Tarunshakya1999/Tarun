# Generated by Django 5.1.2 on 2024-12-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_gamingconsole_earphonescategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamingconsole',
            name='earphonescategory',
            field=models.TextField(choices=[('ps3', 'Playstation3'), ('ps4', 'Playstation4'), ('ps5', 'Playstation5'), ('xb', 'Xbox360'), ('xb', 'XboxSeriesX'), ('xb', 'XboxSeriesS')]),
        ),
    ]
