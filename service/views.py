from service.models import ServiceItem, Order, TeamMember, TrainingService
from django.shortcuts import redirect, render


# Create your views here.

def index(request):
    return render(request, 'service/index.html')

def service_Item(request):
    serviceItem = ServiceItem.objects.all()
    return render(request, 'service/item.html', {'serviceItem' : serviceItem})

def detail(request, id):
    service_item = ServiceItem.objects.get(pk = id)
    return render(request, 'service/service-detail.html', {'service_item' : service_item})

def checkOut(request):
    if request.method == "POST":
        items = request.POST.get('items')
        username = request.POST.get('username',"")
        email = request.POST.get('email')
        address = request.POST.get('address')
        location = request.POST.get('location')
        city = request.POST.get('city')
        fax = request.POST.get('fax')
        gridCheck = request.POST.get('gridCheck')
        if gridCheck == 'on':
            gridCheck = True
        order = Order(items=items, username = username, email = email, address = address, 
        location = location, city = city, fax = fax, gridCheck = gridCheck)
        order.save()
        return redirect('upload')

    return render(request, 'service/checkout.html')

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'service/team-members.html', {'team_members':team_members})


def trainingServices(request):
    
    return render(request, 'service/training-courses.html')


