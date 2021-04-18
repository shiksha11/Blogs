"""IntoTheFuture URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "blogHome"),
    path('blog/', views.blog,name="blogPosts"),
    path('contact/', views.contact,name="ContactUs"),
    path('home/', views.home, name = "blogHome"),
    path('signup/', views.signup, name = "signUp"),
    path('login/', views.login, name = "logIn"),
    path('logout/', views.logOut, name = "logOut"),
    path('blogtemplate/', views.addBlog, name = "addBlog"),
    path('postcomments/', views.postComment, name = "postComment"),
    path('<str:slug>/',views.blogpost,name = "blogPost"),
]
