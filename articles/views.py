from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def greeting(request):
    foods = ['apple','banana','coconut',]
    info = {
        'name':'Alice'
    }
    context={
        'foods':foods,
        'info':info,
    }
    return render(request, 'greeting.html', context)

def throw(request):
    return render(request, 'throw.html')