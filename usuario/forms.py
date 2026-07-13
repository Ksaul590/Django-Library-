import re
from datetime import date
from django import forms
from django.contrib.auth.models import User
from .models import Usuario


class RegistroUsuarioForm(forms.Form):
    cedula = forms.CharField(max_length=10,label="Cédula" )
    nombres = forms.CharField( max_length=100,label="Nombres")
    apellidos = forms.CharField(max_length=100,label="Apellidos")
    correo = forms.EmailField(label="Correo electrónico")
    telefono = forms.CharField(max_length=10,label="Teléfono")
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}),label="Fecha de nacimiento")
    direccion = forms.CharField(widget=forms.Textarea,label="Dirección")
    password = forms.CharField(widget=forms.PasswordInput,label="Contraseña")
    confirmar_password = forms.CharField(widget=forms.PasswordInput,label="Confirmar contraseña")

    def clean_cedula(self):
        cedula = self.cleaned_data["cedula"].strip()
        if not cedula.isdigit():
            raise forms.ValidationError("La cédula solo puede contener números.")
        if len(cedula) != 10:
            raise forms.ValidationError("La cédula debe tener exactamente 10 dígitos.")
        if Usuario.objects.filter(cedula=cedula).exists():
            raise forms.ValidationError("La cédula ya está registrada.")
        return cedula

    def clean_nombres(self):
        nombres = self.cleaned_data["nombres"].strip()
        if len(nombres) < 2:
            raise forms.ValidationError("Ingrese un nombre válido.")

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombres):
            raise forms.ValidationError("Los nombres solo pueden contener letras.")
        return nombres.title()

    def clean_apellidos(self):
        apellidos = self.cleaned_data["apellidos"].strip()
        if len(apellidos) < 2:
            raise forms.ValidationError("Ingrese un apellido válido.")
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", apellidos):
            raise forms.ValidationError("Los apellidos solo pueden contener letras.")
        return apellidos.title()

    def clean_correo(self):
        correo = self.cleaned_data["correo"].strip().lower()
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError(
                "Este correo ya está registrado."
            )
        return correo

    def clean_telefono(self):
        telefono = self.cleaned_data["telefono"].strip()
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono solo puede contener números." )
        if len(telefono) != 10:
            raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
        if not telefono.startswith("09"):
            raise forms.ValidationError("El teléfono debe comenzar con 09.")
        return telefono

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data["fecha_nacimiento"]
        if fecha > date.today():
            raise forms.ValidationError("La fecha no es valida")
        edad = date.today().year - fecha.year

        if edad < 12:
            raise forms.ValidationError(
                "Debe tener al menos 12 años."
            )
        return fecha

    def clean_direccion(self):
        direccion = self.cleaned_data["direccion"].strip()
        if len(direccion) < 2:
            raise forms.ValidationError(
                "La dirección es demasiado corta.")
        return direccion

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar = cleaned_data.get("confirmar_password")
        if password and confirmar:
            if password != confirmar:
                raise forms.ValidationError("Las contraseñas no coinciden.")
            if len(password) < 8:
                raise forms.ValidationError("La contraseña debe tener mínimo 8 caracteres.")
        return cleaned_data