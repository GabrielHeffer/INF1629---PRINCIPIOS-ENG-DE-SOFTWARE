from django.shortcuts import render
from .models import Request


def index(request):
    return render(request, 'index.html')


def info(request):
    requests_base = Request.object.all()
    context = {request.nome: request.urlBase for request in requests_base}
    return render(request, 'info.html', context)
