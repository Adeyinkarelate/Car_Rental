from django.shortcuts import render , get_object_or_404 , redirect
from .models import Car , Brand
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import BrandForm


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

def brand(request):
    brands = Brand.objects.order_by('-date_created')
    context ={
        'brands':brands ,
        }
    return render(request,'car_app/brand.html', context)


def brand_update(request,id):
    brand = get_object_or_404(Brand,id=id)
    form = BrandForm(request.POST or None , instance= brand)
    if request.method == 'POST':
        form = BrandForm(request.POST or None , instance= brand)
        if form.is_valid():
            form.save()
            # message
            return redirect('brand')
        else:
          form = BrandForm(request.POST)  
          
    context = {
        'brand':brand,
        'form':form
    }
    return render(request, 'car_app/brand_update.html', context)

# delete brand 

def brand_delete(request,id):
    brand = get_object_or_404(Brand,id=id)
    # message
    brand.delete()
    return redirect('brand')

# ====================================================================