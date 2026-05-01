from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def service(request):
    return render(request,"main/service.html")

def project(request):
    return render(request,"main/project.html")

def contact(request):
    return render(request,"main/contact.html")

def area_we_serve(request):
    return render(request,"main/area_we_serve.html")

def new_york_project(request):
    return render(request,"main/new_york_project.html")

def new_jersey_project(request):
    return render(request,"main/new_jersey_project.html")

# def testimonial(request):
#     return render(request,"main/testimonial.html")