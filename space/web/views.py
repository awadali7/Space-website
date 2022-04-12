from http.client import HTTPResponse
from importlib.resources import path
from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return render(request,"index.html")

