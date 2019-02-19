"""zy_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
# from blog_user import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog_user/',include('blog_user.urls')),
    path('blog_article/',include('blog_article.urls')),
    path('read_num/',include('read_num.urls')),
    path('likes/',include('likes.urls')),
    path('comment/',include('comment.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),




    path('',include('blog_user.urls')),
]
