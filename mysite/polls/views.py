from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, Mundo. Estas en el indice de las encuestras.")
