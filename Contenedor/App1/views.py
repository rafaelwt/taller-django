from django.shortcuts import render, get_object_or_404
from .models import AutorDb, FraseDb
# from django.http import HttpResponse
# Create your views here.


def index_view(request):
    '''This is the index view of the app1'''
    # return HttpResponse('Hello, World!')
    objeto = AutorDb.objects.all().order_by("-id")
    return render(request, 'index.html', {'objeto': objeto, 'titulo': 'Autores'})


def autor_view(request, id):
    '''This is the autor view of the app1'''
    autor = get_object_or_404(AutorDb, id=id)
    return render(request, 'autor.html', {'objeto': autor})
    # objeto = AutorDb.objects.get(id=id)
    # frases = FraseDb.objects.filter(autor=objeto)
    # return render(request, 'autor.html', {'objeto': objeto, 'frases': frases, 'titulo': 'Frase de ' + objeto.nombre})
