from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('user','first_name', 'last_name','image','gender', 'email','worked_for', 
    'location','water','lunch', 'dinner','brakefast', 'refreshment', 'block', 'dorm')