# Generated by Django 5.1.2 on 2024-12-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_monitor_delete_laptops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='monitorcategory',
            field=models.TextField(choices=[('sm', 'Samsung'), ('ac', 'Accer'), ('ms', 'MSI'), ('ap', 'Apple'), ('gb', 'Gigabyte'), ('ln', 'Lenovo'), ('lg', 'LG')]),
        ),
    ]
