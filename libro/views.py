from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libro/listar.html', {'libros': libros})


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()

    return render(request, 'libro/crear.html', {'form': form})


def editar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'libro/editar.html', {'form': form})


def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)

    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')

    return render(request, 'libro/eliminar.html', {'libro': libro})