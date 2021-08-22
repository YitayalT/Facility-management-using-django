# Generated by Django 3.2.3 on 2021-08-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_trainingservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultancyService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(default='a@yahoo.com', max_length=100)),
            ],
        ),
    ]