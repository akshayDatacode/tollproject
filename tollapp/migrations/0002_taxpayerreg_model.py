# Generated by Django 2.1.5 on 2019-03-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tollapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxpayerReg_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleno', models.CharField(max_length=100)),
                ('taxpayername', models.CharField(max_length=255)),
                ('vtype', models.CharField(max_length=255)),
            ],
        ),
    ]