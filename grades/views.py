from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def show(request):
    return render(request , 'grades/show.html' )

def grades(request):
    if request.user.is_authenticated:        
        grades = random.randint(0,10)
        return render(request, 'grades/show.html', {'grades': grades})
    return redirect('login')