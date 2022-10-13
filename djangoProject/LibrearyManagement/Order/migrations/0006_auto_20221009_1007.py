# Generated by Django 3.2.12 on 2022-10-09 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUser', '0003_auto_20221007_0807'),
        ('Order', '0005_orderdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AdminUser.mybasemodel')),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('password', models.IntegerField()),
                ('signature', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=50)),
            ],
            bases=('AdminUser.mybasemodel',),
        ),
        migrations.AlterModelOptions(
            name='orderdetail',
            options={'verbose_name': 'Order Details', 'verbose_name_plural': 'Order Detail'},
        ),
    ]