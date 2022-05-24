from django.shortcuts import render,HttpResponse

# Create your views here.
from carrito.carro import Carro

def home(request):
    carro=Carro(request)
    return render(request,"Appweb/home.html")



       

      
