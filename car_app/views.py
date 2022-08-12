from django.shortcuts import render , get_object_or_404 , redirect
from .models import Car , Brand , Booking
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import BrandForm , BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import User 
from pages.models import Contact

# =============================CAR=================================
def car_list(request):
    cars = Car.objects.all()
    paginatior = Paginator(cars,4)
    page = request.GET.get('page')
    paged_car = paginatior.get_page(page)
    context = {
        'cars':paged_car,
       
    }
    return render(request, 'car_app/car.html', context)

# car detail 
def car_detail(request,id):
    car = get_object_or_404(Car, id=id)
    context = {
        'car':car
    }
    return render(request,'car_app/car_detail.html',context)
# ==================================================================

# ==================SEARCH===========================================================
def search(request):
    cars = Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(car_category__icontains=keyword)
        else:
            pass
    context ={
        'cars':cars
    }
    return render(request,'car_app/search.html', context)
# =======================================================================

# =========================BRAND=========================================

@login_required
def brand(request):
    brands = Brand.objects.order_by('-date_created')
    car_count = Car.objects.all().count()
    booking_count = Booking.objects.all().count()
    brand_count = Brand.objects.all().count()
    user_count = User.objects.all().count()
    contact_count = Contact.objects.all().count()

    if request.method == 'POST':
        form = BrandForm(request.POST )
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully created new brand')
            return redirect('brand')
    else:
        form = BrandForm() 
    context ={
        'brands':brands ,
        'form':form,
         'car_count':car_count,
         'booking_count':booking_count,
         'brand_count':brand_count,
         'user_count':user_count,
         'contact_count':contact_count,
        }
    return render(request,'car_app/brand.html', context)

@login_required
def brand_update(request,id):
    brand = get_object_or_404(Brand,id=id)
    form = BrandForm(request.POST or None , instance= brand)
    if request.method == 'POST':
        form = BrandForm(request.POST or None , instance= brand)
        if form.is_valid():
            form.save()
            brand_update = f'You have update {brand.brand_name} brand'
            messages.error(request,brand_update)
            return redirect('brand')
        else:
          form = BrandForm(request.POST)  
          
    context = {
        'brand':brand,
        'form':form
    }
    return render(request, 'car_app/brand_update.html', context)

# delete brand 
@login_required
def brand_delete(request,id):
    brand = get_object_or_404(Brand,id=id)
    # message
    brand.delete()
    brand_delete = f'You deleted {brand.brand_name} brand'
    messages.error(request,brand_delete)
    return redirect('brand')



# ============================ADMIN PAGE========================================

# ===============================BOOKING==============================================
def booking(request, id):
    car = get_object_or_404(Car , id=id)
    form = BookingForm(request.POST or None)
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user 
            instance.car = car
            instance.save()
            messages.success(request,'You have successfull booked the car')
            return redirect('home')
        else:
            form = BookingForm(request.POST)
    context = {
        'car':car,
        'form':form
    }
    return render(request,'car_app/booking.html', context)
