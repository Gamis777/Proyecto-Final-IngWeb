from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def Formulario_correos(request):
    return render(request,"Formulario_correos.html")

def contactar(request):
    if request.method=="POST":
        asunto = request.POST["asunto"]
        mensaje =request.POST["mensaje"] + " " + request.POST["email"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["gabrielamis777@gmail.com"]
        send_mail(asunto, mensaje, email_desde,email_para)
        return render(request,"contactar.html")
    return render(request,"Formulario_correos.html")


