# Generated by Django 4.1.13 on 2024-01-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
