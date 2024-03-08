from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.views.decorators.cache import never_cache


# Create your views here.
@never_cache
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = auth.authenticate(request, username=username, password=password)
        if my_user is not None:
            auth.login(request, my_user)
            return redirect('home')
        else:
            messages.error(request, 'The Username or the Password is incorrect. ')
            return redirect ('login_page')
    return render(request, 'login.html')

@never_cache
def log_out(request):
        auth.logout(request)
        return redirect('login_page') 


@never_cache
def home(request):
     if request.user.is_authenticated:
        return render(request, 'home_page.html')
     else:
         return redirect('login_page')