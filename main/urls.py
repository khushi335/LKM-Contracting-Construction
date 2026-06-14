from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("service/",service,name="service"),
    path("project/",project,name="project"),
    path("contact/",contact,name="contact"),
    path("area_we_serve/",area_we_serve,name="area_we_serve"),
    path("new_york_project/",new_york_project,name="new_york_project"),
    path("new_jersey_project/",new_jersey_project,name="new_jersey_project"),
    # --- Existing Structural Routes ---
    path('general-construction/', views.general_construction, name='general_construction'),
    path('demolition-and-building-services/', views.demolition_building, name='demolition_building'),
    path('excavation/', views.excavation, name='excavation'),
    path('steel-structural/', views.steel_structural, name='steel_structural'),
    path('framing/', views.framing, name='framing'),

    # --- Existing Foundation Routes ---
    path('concrete-footing/', views.footing, name='concrete_footing'),
    path('waterproofing/', views.waterproofing, name='waterproofing'),
    path('backfilling/', views.backfilling, name='backfilling'),
    path('hvac-projects/', views.hvac, name='hvac_projects'),

    # --- Existing Finishing Routes ---
    path('roofing/', views.roofing, name='roofing'),
    path('decks/', views.decks, name='decks'),
    path('flooring/', views.flooring, name='flooring'),
    path('painting/', views.painting, name='painting'),

    # --- NEW: MEP & Systems Routes ---
    path('insulation/', views.insulation, name='insulation'),
    path('plumbing-work/', views.plumbing_work, name='plumbing_work'),
    path('electrical-work/', views.electrical_work, name='electrical_work'),
    path('fire-alarm-system/', views.fire_alarm_system, name='fire_alarm_system'),

    # --- NEW: Exterior & Remodeling Routes ---
    path('design-and-build/', views.design_and_build, name='design_and_build'),
    path('bathroom-remodeling/', views.bathroom_remodeling, name='bathroom_remodeling'),
    path('kitchen-remodeling/', views.kitchen_remodeling, name='kitchen_remodeling'),
    path('stucco/', views.stucco, name='stucco'),
    path('windows-and-doors/', views.windows_doors, name='windows_doors'),
    path('gutter-systems/', views.gutter, name='gutter'),
    path('garages-and-doors/', views.garages, name='garages'),
]