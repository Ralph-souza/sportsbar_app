# Generated by Django 3.1.6 on 2021-02-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(blank=True, choices=[('ENTERTAINMENT', 'Entertainment'), ('BEVERAGE', 'Beverage'), ('FOOD', 'Food')], max_length=100),
        ),
    ]
