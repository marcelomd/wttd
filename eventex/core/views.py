# coding: utf-8
from django.http import HttpResponse

def home(request):
    return HttpResponse('Bem vindo ao Eventex!')
