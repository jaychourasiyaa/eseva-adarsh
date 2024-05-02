# Generated by Django 5.0.3 on 2024-04-03 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_finddlnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindAyushmanCardPdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_profe', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=12)),
                ('enter_details', models.CharField(max_length=12)),
                ('mobile_number', models.CharField(max_length=12)),
                ('status', models.IntegerField(default=0)),
                ('upload_file', models.ImageField(upload_to='media/AyushmanCardpdf')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
    ]
