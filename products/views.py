
from django.shortcuts import render, HttpResponse
from .models import Product

def products(request):
    # Liste de produits (tu peux plus tard les prendre depuis une base de données avec un Model)
    liste_produits = Product.objects.all()  # Récupère tous les produits

    # On envoie la liste au template
    return render(request, "liste.html", {"produits": liste_produits})


def home(request):
    myList = [43,34,11, 56]
    return render(request, 'index.html', {"list":myList})

def contact(request):
    return render(request, 'contact.html')

def acceuil(request):
    return render(request, "acceuil.html")

def blog(request):
    return HttpResponse("blog page")

def course(request):
    return render(request, 'course.html')