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

def general_construction(request):
    return render(request, 'main/general_construction.html')
    
def demolition_building(request):
    return render(request, 'main/demolition_building.html')
    
def excavation(request):
    return render(request, 'main/excavation.html')
    
def steel_structural(request):
    return render(request, 'main/steel_structural.html')
    
def framing(request):
    return render(request, 'main/framing.html')
    
def footing(request):
    return render(request, 'main/concrete_footing.html')
    
def waterproofing(request):
    return render(request, 'main/waterproofing.html')
    
def backfilling(request):
    return render(request, 'main/backfilling.html')
    
def hvac(request):
    return render(request, 'main/hvac_projects.html')
    
def roofing(request):
    return render(request, 'main/roofing.html')
    
def decks(request):
    return render(request, 'main/decks.html')
    
def flooring(request):
    return render(request, 'main/flooring.html')
    
def painting(request):
    return render(request, 'main/painting.html')