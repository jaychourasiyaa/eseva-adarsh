# Generated by Django 5.0.3 on 2024-03-30 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_incomecertificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomicalCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('samagr_id', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=12)),
                ('status', models.IntegerField(default=0)),
                ('upload_file', models.ImageField(upload_to='media/Domicalcertificate')),
                ('download_file', models.ImageField(upload_to='media/Domicalcertificate')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
    ]
