# Generated by Django 2.1.5 on 2019-02-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TollCmpReg_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tollid', models.CharField(max_length=100)),
                ('tollcmpname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
