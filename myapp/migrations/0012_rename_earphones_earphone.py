# Generated by Django 5.1.2 on 2024-12-10 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_monitorcategory_earphones_earphonescategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Earphones',
            new_name='Earphone',
        ),
    ]
