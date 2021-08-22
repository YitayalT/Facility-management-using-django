from django.contrib import admin
from .models import ServiceItem, Order,TeamMember,TrainingService, ConsultancyService
# Register your models here.
admin.site.site_header = 'FMS Administration'
admin.site.site_title = 'managing services'
admin.site.index_title = 'Manage ALA services'
admin.site.register(ServiceItem)
admin.site.register(Order)
admin.site.register(TeamMember)
admin.site.register(TrainingService)
admin.site.register(ConsultancyService)
