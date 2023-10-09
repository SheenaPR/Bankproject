from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import CustomerForm
from .models import CustomerDetails
# Create your views here.

def demo(request):
    return render(request,"index.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('start')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
        return redirect('start')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken!")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                print("User created")
                return redirect('login')
        else:
            messages.info(request,"Passwords don't match!")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def start(request):
    return render(request,"start.html")

def form(request):
    if request.method=='POST':
        cust_form = CustomerForm(request.POST)
        if cust_form.is_valid():
            obj = CustomerDetails()
            obj.first_name =cust_form.cleaned_data['first_name']
            obj.last_name =cust_form.cleaned_data['last_name']
            obj.age =cust_form.cleaned_data['age']
            obj.gender =cust_form.cleaned_data['gender']
            obj.phone_no =cust_form.cleaned_data['phone_no']
            obj.address =cust_form.cleaned_data['address']
            obj.district =cust_form.cleaned_data['district']
            obj.branch =cust_form.cleaned_data['branch']
            obj.account_type =cust_form.cleaned_data['account_type']
            obj.materials_req =cust_form.cleaned_data['materials_req']
            obj.save()
        return redirect('final')

    return render(request,"form.html")


def final(request):

    return render(request,"final.html")