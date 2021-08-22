from django.db import models
from import_export import resources
from .models import Profile

class PersonResource(resources.ModelResource):
    class Meta:
       model = Profile