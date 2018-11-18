from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    return HttpResponse("程鹏 LOVE 卢萍萍")


# Create your views here.
