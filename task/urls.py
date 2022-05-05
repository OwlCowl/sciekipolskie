"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from sciekipolskie.views import RepresentList, AddNewWorkerView, DetailsAboutWorkerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RepresentList.as_view(), name='main_list'),
    path('employee/new/', AddNewWorkerView.as_view(), name='add_new_employee'),
    path('employee/details/<int:id_of_worker>/', DetailsAboutWorkerView.as_view(), name='details_about_employee'),
]
