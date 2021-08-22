from django.db import models
from django import forms
from django.db.models.fields import BooleanField
# Create your models here.

class ServiceItem(models.Model):
    image = models.ImageField(default='google.jpg', upload_to = 'profile_pictures')
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.CharField(max_length=20)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name


class Order(models.Model):
    items = models.CharField(max_length=100, default= 'null')
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    gridCheck = BooleanField()
    
    def __str__(self):
        return self.items
    
class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='google.jpg', upload_to = 'profile_pictures')
    role = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class TrainingService(models.Model):
    work_ethics_altitude = models.BooleanField(null = True)
    mind_set = models.BooleanField(null = True)
    project_management = models.BooleanField(null = True)

class ConsultancyService(models.Model):
    ProjectDesign_preparation = models.BooleanField(null = True)
    EnvironmentalImpactAssessment = models.BooleanField(null = True)
    FeasibilityStudy = models.BooleanField(null = True)
    ProposalPreparation = models.BooleanField(null = True)
    BusinessPlan_preparation = models.BooleanField(null = True)
    OrganizationalStructure = models.BooleanField(null = True)
    SalaryScalePreparation = models.BooleanField(null = True)
    JobEvaluationAndGrading = models.BooleanField(null = True)
    StrategicPlanningManagement = models.BooleanField(null = True)
    TrainingNeedAssessmentSurvey = models.BooleanField(null = True)
    ReformImplementation = models.BooleanField(null = True)
    OthersDocumentPreparation = models.BooleanField(null = True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='a@yahoo.com')

    def __str__(self):
        return self.username