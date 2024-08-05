from django.shortcuts import render
from django.http import HttpResponse
from .models import Collection, piece

def index(request):
    all_collections = Collection.objects.all()
    print("All collections:", all_collections)  # Debug print to check data retrieval
    for collection in all_collections:
        print(collection.collection_name, collection.description)  # Print each collection's name and description
    context = {
        "all_collections": all_collections
    }
    return render(request, "genre/genretemplate.html", context)

def details(request, collection_id):
    return HttpResponse(f"<h1>The collection id is: {collection_id}</h1>")
