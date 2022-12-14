# Generated by Django 4.0.4 on 2022-08-06 12:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0005_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=220)),
                ('mobile_no', models.BigIntegerField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 8, 6, 18, 12, 45, 325543))),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipkart.registration')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipkart.product')),
            ],
        ),
    ]
