from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Profile
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
# Create your views here.

def register(request):
    if request.method == 'POST':
        print(f'the requested method is {request.POST}')
        form = RegisterForm(request.POST)
        print(f'the {request.method}ed value is {request.POST}')
        if form.is_valid():
            form.save()

            return redirect('service:training_service')
    else:
     form = RegisterForm()

    return render(request, 'users/register.html', { 'form' : form})

@login_required
def profilePage(request):
    user_profile = Profile.objects.all()
    # print(user_profile.first_name)
    return render(request, 'users/profile.html',{'user_profile':user_profile})
    
    
def simpleUpload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myFile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'wrong file format')
            return render(request, 'users/upload.html')
        imported_data = dataset.load(new_person.read(), format='xlsx')
        
        for data in imported_data:
            value = Profile(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
            )
            value.save()
        return redirect('service:index')
    return render(request, 'users/upload.html')



   
