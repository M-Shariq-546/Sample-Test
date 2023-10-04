from django.shortcuts import render
from .models import Details

def details(request):
    det = Details.objects.all()
    data = {
        "details":det,
    }
    return render(request , "welcome.html", data)
# Create your views here.
