# Generated by Django 5.0.3 on 2024-04-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_detailstopdf_is_valid_detailstopdf_prev_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_id', models.CharField(max_length=100)),
                ('secret_key', models.CharField(max_length=100)),
            ],
        ),
    ]