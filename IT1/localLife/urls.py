"""localLife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from pages.views import home_view, contact_view, about_view, profile_view
from products.views import search
from register import views as v
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from django.urls import path
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('profile/', profile_view),
    path('about/', about_view),
    path('admin/', admin.site.urls),
    path('s/', search, name='search'),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    # path("login", v.login_request, name="login"),
    path('login/', views.LoginView.as_view(), name='login'),
    path("logout", v.logout_request, name="logout"),
    path('profile/', user_views.profile, name='profile'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
    # Products App
    path('products/', include('products.urls')),

    # Store App
    path('', include('store.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
