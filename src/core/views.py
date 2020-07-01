from django.shortcuts import render
from .models import Request


def index(request):
    return render(request, 'index.html')


def resultado(request):
    all_requests = Request.objects.all()
    context = {request.nome: request.urlBase for request in all_requests}
    context.update({request.nome+'OBD': request.urlBase + request.OBdata for request in all_requests})
    return render(request, 'resultado.html', context)
