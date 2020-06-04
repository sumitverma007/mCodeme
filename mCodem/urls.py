"""mCodem URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('meme/',include('meme.urls')),
    path('problem/',include('problem.urls')),
    path('handleLogin/',views.handleLogin,name="login"),
    path('handleSignup/',views.handleSignup,name="Signup"),
    path('handleLogout/',views.handleLogout,name="logout"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
