# Generated by Django 4.0.4 on 2022-07-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
