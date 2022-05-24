from django.shortcuts import render,redirect

from.forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()

      # aqui se rescata la informacion de contacto que envia el usario y la envia a las variables definidas dentro del if
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            celular=request.POST.get("celular")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Tienda Electronica SIP.electronic",
            "El Usuario con nombre {} con la direccion {} escribe los siguiente:\n\n {}".format(nombre,email,contenido),
            "",["juandcg271@gmail.com"],reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")




    return render(request,"contacto/contacto.html",{'miFormulario':formulario_contacto})


    