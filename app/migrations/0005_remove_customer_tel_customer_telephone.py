# Generated by Django 4.2 on 2023-04-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='tel',
        ),
        migrations.AddField(
            model_name='customer',
            name='telephone',
            field=models.CharField(max_length=45, null=True),
        ),
    ]