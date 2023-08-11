from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    
    path("", views.index,name='index'),
    path("usuario/login", views.login_view,name='login'),
    path("usuario/logout", views.logout_view,name='logout'),
    path("usuario/registro", views.register,name='register'),
    path('admin/', admin.site.urls),
]
