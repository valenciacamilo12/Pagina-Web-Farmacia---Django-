"""src URL Configuration

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
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, password_reset, password_reset_done,password_reset_confirm, password_reset_complete, logout_then_login
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^productos/', include('apps.productos.urls', namespace='productos')),
    url(r'^usuarios/', include('apps.usuario.urls', namespace='usuarios')),
    url(r'^empleados/', include('apps.empleados.urls', namespace='empleados')),
    url(r'^$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/login/', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)