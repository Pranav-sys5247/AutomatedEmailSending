from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages



def registration(request):
    form=CustomUserCreationForm()
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('login/Registration/')
        else:
            messages.info(request,"Password does not match")
       
    return render(request,"registration.html",{'form':form})
def authentication(request):
    if request.method=="POST":
       username=request.POST.get("username")
       password=request.POST.get("password1")
       user=authenticate(request,username=username,password=password)
       if user is not None:
          login(request,user)
          return redirect('Registration/')
       else:
           messages.info(request,"Username or Password is incorrect")
    return render(request, "registration.html")
   
# Create your views here.
