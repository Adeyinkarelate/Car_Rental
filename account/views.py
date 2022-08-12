from django.contrib import messages, auth
from .forms import ProfileForm , EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import redirect , render


# Create your views here.
# =========================================================== REGISTER ===========================================================
def register(request):    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Login successfully')
            return redirect('login')
    else:
        form = ProfileForm()       
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)


# =========================================login====================================================
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # admin
        if user is not None and user.is_staff:
            if user.is_active:
                login(request, user)
                return redirect('brand')   #this is where the admin will go if it was the admin that login
            else:                
                messages.warning(request, 'Account is not active')
                return render(request, 'account/login.html')      

        #  the normal user
        elif user is not None and not user.is_staff  :
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:                
                messages.warning(request, 'Account is not active')
                return render(request, 'account/login.html')  

        else:
            messages.error(request, 'Please enter valid details')
            return render(request, 'account/login.html')

    else:
        return render(request, 'account/login.html')    


# ===================================logout 
@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')


# ==========Edit profile=======================

@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = EditProfileForm(request.POST or None, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            profile_form.save()
            if request.user.is_authenticated and request.user.is_staff:
                messages.success(request, 'Editted successfully')
                return redirect('brand')
            elif request.user.is_authenticated and not request.user.is_staff:
                messages.success(request, 'Editted successfully')
                return redirect('home')
            

    else:
       profile_form = EditProfileForm(instance = request.user)

    context = {
        'profile_form': profile_form
    }

    return render(request, 'account/edit_profile.html', context)