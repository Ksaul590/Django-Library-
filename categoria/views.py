from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm


def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/listar.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'categoria/crear.html', {'form': form})


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'categoria/editar.html', {'form': form})


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')

    return render(request, 'categoria/eliminar.html', {'categoria': categoria})