from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("service/",service,name="service"),
    path("project/",project,name="project"),
    path("contact/",contact,name="contact"),
    path("area_we_serve/",area_we_serve,name="area_we_serve"),
    path("new_york_project/",new_york_project,name="new_york_project"),
    path("new_jersey_project/",new_jersey_project,name="new_jersey_project"),
    # path("testimonial/",testimonial,name="testimonial"),
    path('general-construction/', general_construction, name='general_construction'),
    path('demolition-and-building-services/', demolition_building, name='demolition_building'),
    path('excavation/', excavation, name='excavation'),
    path('steel-structural/', steel_structural, name='steel_structural'),
    path('framing/', framing, name='framing'),
    path('concrete-footing/', footing, name='concrete_footing'),
    path('waterproofing/', waterproofing, name='waterproofing'),
    path('backfilling/', backfilling, name='backfilling'),
    path('hvac-projects/', hvac, name='hvac_projects'),
    path('roofing/', roofing, name='roofing'),
    path('decks/', decks, name='decks'),
    path('flooring/', flooring, name='flooring'),
    path('painting/', painting, name='painting'),
]