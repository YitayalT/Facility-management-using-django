# Generated by Django 3.2.3 on 2021-08-20 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
