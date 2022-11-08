from django.shortcuts import render
from django.http import HttpResponse
from Family.models import Familiar
from django.template import Template, Context
# Create your views here.

def datos_familia(request):
    archivo = open(r"C:\Users\JuanCarlos\Desktop\Python\MVT_JuanCarlosNieto\DesafioMTV\template\template1.html")
    
    plantilla = Template(archivo.read())

    archivo.close()

    familiar = Familiar.objects.all()

    cad_flia = ""

    for flia in familiar:
        cad_flia += (f"{flia.nombre} {flia.apellido}: (DNI:{flia.dni});(Parentesco:{flia.parentesco})" + ",")
    
    cad_flia = cad_flia.split(",")

    datos = {"info":cad_flia}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
