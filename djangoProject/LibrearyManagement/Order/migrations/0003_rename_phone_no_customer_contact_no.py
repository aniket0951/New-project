# Generated by Django 3.2.12 on 2022-10-07 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20221007_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone_no',
            new_name='contact_no',
        ),
    ]