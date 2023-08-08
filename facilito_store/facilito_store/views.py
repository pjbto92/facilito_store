from django.http import HttpResponse

def index (request):
        return HttpResponse('Hola Mundo desde el archivo views.py')