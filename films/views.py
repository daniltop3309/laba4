from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from films.models import Films, Category


def index(request):
    films = Films.objects.all()
    return render(request, 'films/index.html', {'films': films})


def create(request):
    create_categories()
    if request.method == "POST":
        films = Films()
        films.name = request.POST.get("name")
        films.release_date = request.POST.get("release_date")
        films.actors = request.POST.get("actors")
        films.show_date = request.POST.get("show_date")
        films.category_id = request.POST.get("category")
        films.save()
        return redirect("home")

    categories = Category.objects.all()
    return render(request, "films/create.html", {"categories": categories})


def delete(request, id):
    try:
        film = Films.objects.get(id=id)
        film.delete()
        return redirect('home')
    except:
        return HttpResponseNotFound('<h2>Film not found</h2>')


def create_categories():
    if Category.objects.all().count() == 0:
        Category.objects.create(name="Боевик")
        Category.objects.create(name="Драма")