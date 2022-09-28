# Generated by Django 4.0.4 on 2022-07-25 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=500)),
                ('pro_image', models.ImageField(upload_to='upload/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipkart.category')),
            ],
        ),
    ]
