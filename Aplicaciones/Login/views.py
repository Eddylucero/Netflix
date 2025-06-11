from django.shortcuts import render, redirect
from .models import Usuario

def index(request):
    return render(request, 'Inicio/index.html') 

def error_usuario(request):
    return render(request, 'Inicio/error.html')

def agregar_usuario(request):
    if request.method == "POST":
        correo = request.POST.get("correo", "").strip()
        password = request.POST.get("password", "").strip()

        if correo and password:  # ✅ Si los campos están llenos, guarda los datos
            Usuario.objects.create(correo=correo, password=password)
        
        return redirect('error_usuario')  # ✅ Redirige siempre a `error.html`

    return render(request, "Inicio/index.html")