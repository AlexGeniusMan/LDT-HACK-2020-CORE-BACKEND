"""core_service URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import main_app.views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),

    path('api/get_status', main_views.CoursePage.as_view()),                    # get

    path('api/my_classes', main_views.ShowMyClasses.as_view()),                 # get

    path('api/classes/<int:pk>/', main_views.ShowClass.as_view()),              # get

    path('api/classes/<int:pk>/new_block', main_views.CreateBlock.as_view()),   # post
    path('api/blocks/<int:pk>/delete', main_views.DeleteBlock.as_view()),       # delete
    path('api/blocks/<int:pk>/change', main_views.ChangeBlock.as_view()),       # put

    path('api/tasks/<int:pk>/', main_views.ShowTask.as_view()),                 # get
    path('api/blocks/<int:pk>/new_task', main_views.CreateTask.as_view()),      # post
    path('api/tasks/<int:pk>/delete', main_views.DeleteTask.as_view()),         # delete
    path('api/tasks/<int:pk>/change', main_views.ChangeTask.as_view()),         # put

    path('api/tasks/<int:pk>/send_code', main_views.CodeChecker.as_view()),     # post
]
