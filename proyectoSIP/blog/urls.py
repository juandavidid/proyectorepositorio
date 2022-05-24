from django.urls import path

from .import views



urlpatterns = [
    

    # Agregamos la url del app productos
    
    
    path('',views.blog, name="blog"),
    
] 