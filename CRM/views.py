from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.


def home(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "You have been Logged in")
            return redirect('home')
        else:
           messages.success(request, "There was an error logging in, please try again") 
           return redirect('home')
    else:
        return render(request, "website/home.html")

def login(request):
    pass

 
def logout(request):
    auth_logout(request)
    messages.success(request, "You Have been Logged out...")
    return render(request, "website/home.html")


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            auth_login(request, user)
            messages.success(request, "You Have Successfully Registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, "website/register.html", {'form': form})
    return render(request, "website/register.html", {'form': form})
