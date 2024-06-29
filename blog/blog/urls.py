"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from blog.views import PostListCreateView, PostDetailView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    # path('api/', views.api_root, name='api_root'),
    # path('api/posts/', views.api_posts, name='api_posts'),
    # path('api/posts/<int:id>/', views.api_post_by_id, name='api_post_by_id')
    path('api/posts/', PostListCreateView.as_view(), name='api_posts'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='api_post_by_id'),

]
