"""django_store URL Configuration

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
<<<<<<< HEAD
from django.urls import path, include
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
=======
<<<<<<< HEAD:src/localLife/urls.py
from django.urls import include, path
from pages.views import home_view, contact_view, about_view
from products.views import search
from register import views as v

from django.conf import settings
from django.conf.urls.static import static
=======
from django.urls import path, include
from store import views as store_views
>>>>>>> cb63af76e6e079dfe5bbd22bbc8f57199ccf9375:IT1/django_store/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD:src/localLife/urls.py
    path('s/', search, name='search'),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),


    # Products App

    path('products/', include('products.urls')),

    # Restaurent App

    # User App

    # Recommendation App

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
>>>>>>> cb63af76e6e079dfe5bbd22bbc8f57199ccf9375
    path('', include('store.urls')),
    path('about/', store_views.about, name='store-about'),
    path('user/', include('users.urls'))
]
<<<<<<< HEAD
=======
>>>>>>> cb63af76e6e079dfe5bbd22bbc8f57199ccf9375:IT1/django_store/urls.py
>>>>>>> cb63af76e6e079dfe5bbd22bbc8f57199ccf9375
