# Generated by Django 3.2.12 on 2022-10-07 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminUser', '0003_auto_20221007_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AdminUser.mybasemodel')),
                ('order_id', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('phone_no', models.IntegerField()),
                ('payment_method', models.CharField(max_length=100)),
                ('order_total', models.IntegerField()),
            ],
            bases=('AdminUser.mybasemodel',),
        ),
    ]
