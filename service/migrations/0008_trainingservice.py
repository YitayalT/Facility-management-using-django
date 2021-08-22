# Generated by Django 3.2.3 on 2021-08-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_ethics_altitude', models.BooleanField(null=True)),
                ('mind_set', models.BooleanField(null=True)),
                ('project_management', models.BooleanField(null=True)),
            ],
        ),
    ]
