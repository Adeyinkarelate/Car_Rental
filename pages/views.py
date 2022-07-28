from django.shortcuts import render , redirect
from .forms import ContactForm
from car_app.models import Car
# Create your views here.
def home(request):
    cars = Car.objects.order_by('created_date').filter(is_latest=True)[:3]
    context ={
        'cars':cars 
    }
    return render(request,'pages/home.html',context)

def about(request):
    context ={}
    return render(request,'pages/about.html',context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            # message
            return redirect('home')
    else:
       form = ContactForm() 
    context ={
        'form':form
    }
    return render(request,'pages/contact.html',context)

def services(request):
    context ={}
    return render(request,'pages/services.html',context)