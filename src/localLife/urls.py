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
from pages.views import home_view, contact_view, about_view
from products.views import search
from register import views as v

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('admin/', admin.site.urls),
    path('s/', search, name='search'),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),


    # Products App

    path('products/', include('products.urls')),

    # Restaurent App

    # User App

    # Recommendation App

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
