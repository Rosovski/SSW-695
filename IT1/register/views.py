# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.

# def register(response):
#     if response.method == "POST":
# 	    form = RegisterForm(response.POST)
# 	    if form.is_valid():
# 	        form.save()

# 	    return redirect("/login")
#     else:
# 	    form = RegisterForm()
    
#     return render(response, "register/register.html", {"form":form}) 

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("/")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "templates/login.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")
