from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib import messages 
from django.contrib.auth import login
from django.contrib.auth import authenticate

def index (request):
        return render (request,'index.html',{
            'message': 'Listado de Productos',
            'title': 'Productos',
            'products': [
                
                {'title':'Playera', 'price': 5, 'stock': True},
                {'title':'Camisa', 'price': 7, 'stock': True},
                {'title':'Mochila', 'price': 20, 'stock': False},
                 {'title':'Laptop', 'price': 120, 'stock': True},
                
                
             ]
        })
        
        
        
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') 
         
        user = authenticate( username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request,'Usuario y contraseña no validos')            

    return render(request,'users/login.html', {})   