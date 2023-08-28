from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

from Products.views import ProductListView




urlpatterns = [
    
    
    path("", ProductListView.as_view(),name='index'),
    path("usuario/login", views.login_view,name='login'),
    path("usuario/logout", views.logout_view,name='logout'),
    path("usuario/registro", views.register,name='register'),
    path('admin/', admin.site.urls),
    path('productos/', include('Products.urls'))   
]
