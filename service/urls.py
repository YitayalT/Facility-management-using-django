
from service import views
from django.urls import path

app_name = 'service'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('service-item', views.service_Item, name = 'service_item'),
    path('<int:id>', views.detail, name = 'service_detail'),
    path('checkout', views.checkOut, name = 'checkout'),
    path('team-member', views.team, name = 'team_member'),
    path('training-service', views.trainingServices, name = 'training_service'),
]