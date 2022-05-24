from django.shortcuts import render

# Create your views here.
from .models import Proveedor

def proveedor(request):
    proveedor=Proveedor.objects.all()
    return render(request,{ "proveedor":proveedor})


