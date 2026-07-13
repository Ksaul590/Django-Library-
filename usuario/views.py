from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from .models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data["correo"],
                first_name=form.cleaned_data["nombres"],
                last_name=form.cleaned_data["apellidos"],
                email=form.cleaned_data["correo"],
                password=form.cleaned_data["password"]
            )

            Usuario.objects.create(user=user,cedula=form.cleaned_data["cedula"],telefono=form.cleaned_data["telefono"],fecha_nacimiento=form.cleaned_data["fecha_nacimiento"],direccion=form.cleaned_data["direccion"])
            messages.success(request,"Usuario registrado correctamente.")
            return redirect("login")
    else:
        form = RegistroUsuarioForm()
    return render(
        request,
        "registration/register.html",
        {"form": form}
    )

def login_view(request):

    if request.method == "POST":
        correo = request.POST.get("correo")
        password = request.POST.get("password")
        user = authenticate(request,username=correo,password=password)

        if user is not None:
            login(request, user)
            return redirect("menu")
        messages.error(request, "Correo o contraseña incorrectos.")
    return render(request, "registration/login.html")

@login_required
def menu(request):
    return render(request, "menu.html")

def logout_view(request):
    logout(request)
    return redirect("login")