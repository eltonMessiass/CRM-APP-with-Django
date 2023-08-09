from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.


def home(request):
    records = Record.objects.all()
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
        return render(request, "website/home.html",{'records':records})

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



def CreateRecord(request):
    form = AddRecordForm(request.POST, request.FILES)

    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'website/add_record.html', {'form':form})
    else:
        return redirect('home')
    

def costumer_record(request, pk):

    if request.user.is_authenticated:
        c_record = Record.objects.get(id=pk)
        return render(request, "website/record.html", {'c_record':c_record})
    else:
        return redirect('home')
    

def edit_record(request, pk):

    if request.user.is_authenticated:
        
        record = Record.objects.get(id=pk)

        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'website/update_record.html', {'form':form})
    else:
        return redirect('home')