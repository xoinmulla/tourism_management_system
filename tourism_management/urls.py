"""
URL configuration for tourism_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from tourism import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tourism.urls')),
    path('tourism/packages/', views.packages, name='packages'),
    path('tourism/destination/', views.destination, name='destination'),
    path('tourism/reviews/', views.reviews, name='reviews'),
    path('tourism/contact/', views.contact, name='contact'),



]


