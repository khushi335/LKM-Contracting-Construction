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
]