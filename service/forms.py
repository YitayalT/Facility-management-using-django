from django import forms
from django.db.models import fields
from .models import TrainingService


class TrainingServiceForm(forms.ModelForm):
    class Meta:
        model = TrainingService
        fields = ('work_ethics_altitude','mind_set', 'project_management')
        
    