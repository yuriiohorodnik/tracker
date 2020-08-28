"""time_tracker URL Configuration

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
from tasks import views

urlpatterns = [
    path('', views.index, name="index"),
    path('edit/', views.edit_task, name="edit_task"),
    path('projects/', views.show_projects, name="show_projects"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('tasks/', views.get_tasks, name="get_tasks"),
    path('admin/', admin.site.urls),
]
