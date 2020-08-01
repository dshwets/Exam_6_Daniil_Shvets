"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from webapp.views import index_view, watch_product, update_product, delete_product, create_feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('feedback/<int:pk>/', watch_product, name='watch_feedback'),
    path('feedback/add/', create_feedback, name='create_feedback'),
    path('feedback/<int:pk>/update/', update_product, name='update_product'),
    path('feedback/<int:pk>/delete/', delete_product, name='product_delete'),
]
