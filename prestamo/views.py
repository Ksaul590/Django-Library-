from django.shortcuts import render, redirect, get_object_or_404
from .models import Prestamo
from .forms import PrestamoForm


def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamo/listar.html', {'prestamos': prestamos})


def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm()

    return render(request, 'prestamo/crear.html', {'form': form})


def editar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, pk=id)

    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)

    return render(request, 'prestamo/editar.html', {'form': form})


def eliminar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, pk=id)

    if request.method == 'POST':
        prestamo.delete()
        return redirect('lista_prestamos')

    return render(request, 'prestamo/eliminar.html', {'prestamo': prestamo})