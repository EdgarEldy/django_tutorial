# Generated by Django 4.2 on 2023-04-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_customer_tel_customer_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='qty',
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
