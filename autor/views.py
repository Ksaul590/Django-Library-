from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'prestamo/listar.html', {'autores': autores})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()

    return render(request, 'autor/crear.html', {'form': form})

def editar_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)

    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)

    return render(request, 'autor/editar.html', {'form': form})

def eliminar_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)

    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')

    return render(request, 'autor/eliminar.html', {'autor': autor})


