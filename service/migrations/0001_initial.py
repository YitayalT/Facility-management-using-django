# Generated by Django 3.2.3 on 2021-08-23 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultancyService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(default='a@yahoo.com', max_length=100)),
                ('ProjectDesign_preparation', models.BooleanField(null=True)),
                ('EnvironmentalImpactAssessment', models.BooleanField(null=True)),
                ('FeasibilityStudy', models.BooleanField(null=True)),
                ('ProposalPreparation', models.BooleanField(null=True)),
                ('BusinessPlan_preparation', models.BooleanField(null=True)),
                ('OrganizationalStructure', models.BooleanField(null=True)),
                ('SalaryScalePreparation', models.BooleanField(null=True)),
                ('JobEvaluationAndGrading', models.BooleanField(null=True)),
                ('StrategicPlanningManagement', models.BooleanField(null=True)),
                ('TrainingNeedAssessmentSurvey', models.BooleanField(null=True)),
                ('ReformImplementation', models.BooleanField(null=True)),
                ('OthersDocumentPreparation', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(default='null', max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('gridCheck', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='google.jpg', upload_to='profile_pictures')),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='google.jpg', upload_to='profile_pictures')),
                ('role', models.CharField(max_length=50)),
            ],
        ),
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
