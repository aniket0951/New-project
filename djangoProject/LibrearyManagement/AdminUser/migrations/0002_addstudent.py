# Generated by Django 3.2.12 on 2022-10-06 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AdminUser.mybasemodel')),
                ('stud_name', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('signature', models.CharField(max_length=100)),
            ],
            bases=('AdminUser.mybasemodel',),
        ),
    ]
