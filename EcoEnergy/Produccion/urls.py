"""
URL configuration for monitoreo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from devices.views import home, device_detail, create_device, device_panel, measurements_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),

    path('', include('users.urls')),
    path('home/', home, name="list_devices"),
    path('devices/panel/', device_panel, name="device_panel"),
    path('devices/<int:device_id>/', device_detail, name="device_detail"),
    path('devices/create/', create_device, name="create_device"),
    path('create/', create_device, name="create_device"),  # <--- aquí la ruta
    path('devices/measurements/', measurements_view, name="measurements"),
]