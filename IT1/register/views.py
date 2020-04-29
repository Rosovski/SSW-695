# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
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

    form = UserRegisterForm
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

@login_required
def profile(request):
    return render(request, 'profile.html')
    
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }

#     return render(request, "profile.html", context)



