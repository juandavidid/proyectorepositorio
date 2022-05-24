from django.urls import path

from proveedor import views



urlpatterns = [
    
    path('',views.proveedor,name="proveedor"),
    
    
]

