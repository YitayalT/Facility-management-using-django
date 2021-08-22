# Generated by Django 3.2.3 on 2021-08-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_serviceitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceitem',
            name='quality_level',
        ),
        migrations.AddField(
            model_name='serviceitem',
            name='image',
            field=models.ImageField(default='google.jpg', upload_to='profile_pictures'),
        ),
    ]
