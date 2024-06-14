from django.shortcuts import render
from django.http import HttpResponse
import pathlib


def home_page_view(request,*args,**kwargs):
    return render(request, "home.html", {})