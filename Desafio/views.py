from django.http import HttpResponse
from django.template import Template, Context
from Family.models import Familiar

def vista_inicio(request):
    archivo = open(r"C:\Users\JuanCarlos\Desktop\Python\MVT_JuanCarlosNieto\DesafioMTV\template\template0.html")

    plantilla = Template(archivo.read())

    archivo.close()

    familiar = Familiar.objects.all()

    cad_flia = ""

    for flia in familiar:
        cad_flia += (f"{flia.nombre}" + ",")
    
    cad_flia = cad_flia.split(",")

    datos = {"nombre":cad_flia}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


