# Generated by Django 3.2.12 on 2022-10-07 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUser', '0002_addstudent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addbook',
            options={'verbose_name': 'Add books', 'verbose_name_plural': 'Add Book'},
        ),
        migrations.AlterModelOptions(
            name='addstudent',
            options={'verbose_name': 'Add Students', 'verbose_name_plural': 'Add Student'},
        ),
    ]