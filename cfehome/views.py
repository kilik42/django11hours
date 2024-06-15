from django.shortcuts import render
from django.http import HttpResponse
import pathlib

from visits.models import PageVisit

def home_page_view(request,*args,**kwargs):
    #queryset = PageVisit.objects.all()  #method to get all the objects from the database
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    for obj in page_qs:
        print(obj.page)

    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 456, 789, "Abc"],
        "queryset": page_qs.count(),
        "total_visit_count": qs.count(),
    }
    path = request.path
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", my_context)

def about_page_view(request,*args,**kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 456, 789, "Abc"],
    }
    return render(request, "about.html", my_context)