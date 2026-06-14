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

# ==========================================
# STRUCTURAL VIEWS
# ==========================================
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


# ==========================================
# FOUNDATION VIEWS
# ==========================================
def footing(request):
    return render(request, 'main/concrete_footing.html')

def waterproofing(request):
    return render(request, 'main/waterproofing.html')

def backfilling(request):
    return render(request, 'main/backfilling.html')

def hvac(request):
    return render(request, 'main/hvac_projects.html')


# ==========================================
# FINISHING VIEWS
# ==========================================
def roofing(request):
    return render(request, 'main/roofing.html')

def decks(request):
    return render(request, 'main/decks.html')

def flooring(request):
    return render(request, 'main/flooring.html')

def painting(request):
    return render(request, 'main/painting.html')


# ==========================================
# NEW: MEP & SYSTEMS VIEWS
# ==========================================
def insulation(request):
    return render(request, 'main/insulation.html')

def plumbing_work(request):
    return render(request, 'main/plumbing_work.html')

def electrical_work(request):
    return render(request, 'main/electrical_work.html')

def fire_alarm_system(request):
    return render(request, 'main/fire_alarm_system.html')


# ==========================================
# NEW: EXTERIOR & REMODELING VIEWS
# ==========================================
def design_and_build(request):
    return render(request, 'main/design_and_build.html')

def bathroom_remodeling(request):
    return render(request, 'main/bathroom_remodeling.html')

def kitchen_remodeling(request):
    return render(request, 'main/kitchen_remodeling.html')

def stucco(request):
    return render(request, 'main/stucco.html')

def windows_doors(request):
    return render(request, 'main/windows_doors.html')

def gutter(request):
    return render(request, 'main/gutter.html')

def garages(request):
    return render(request, 'main/garages.html')