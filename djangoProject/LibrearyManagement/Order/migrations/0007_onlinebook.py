# Generated by Django 3.2.12 on 2022-10-12 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUser', '0003_auto_20221007_0807'),
        ('Order', '0006_auto_20221009_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineBook',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AdminUser.mybasemodel')),
                ('book_name', models.CharField(blank=True, max_length=100)),
                ('book_price', models.IntegerField()),
                ('book_witer', models.CharField(blank=True, max_length=100)),
                ('Author_write_year', models.IntegerField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('AdminUser.mybasemodel',),
        ),
    ]
