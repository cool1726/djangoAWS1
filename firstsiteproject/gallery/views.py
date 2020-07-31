from django.shortcuts import render
from .models import Gallery

# Create your views here.
def gallery(request):
    galleries = Gallery.objects
    return render(request, 'gallery.html', {'galleries':galleries})