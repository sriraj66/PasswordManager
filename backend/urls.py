
from django.contrib import admin
from django.urls import path
from core.views import *
from  django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    
    path('',index,name="index"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',logoutAccount,name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)