from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "template/index.html")

def redes(request):
    return render(request, "template/redes.html")
