# Generated by Django 3.2.3 on 2021-08-18 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_type', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quality_level', models.CharField(max_length=50)),
                ('quantity', models.ImageField(upload_to='')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
