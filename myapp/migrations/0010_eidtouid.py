# Generated by Django 5.0.3 on 2024-04-01 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_uidtopdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='EidtoUid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('eid', models.CharField(max_length=12)),
                ('mobile_number', models.CharField(max_length=12)),
                ('status', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=12)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
    ]
