"""
URL configuration for project2 project.

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
from django.shortcuts import redirect
from django.conf.urls.i18n import i18n_patterns  # Import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('frontend:login')),  # Redirects root URL to login
    path('frontend/', include('frontend.urls')),
    path('spotify/', include('spotify.urls')),
    path('wraps/', include('wraps.urls', namespace='wraps')),
]

