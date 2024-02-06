from django.shortcuts import render

def home(request):
    # Your view logic here
    return render(request, 'home.html')

def login(request):
    # Your view logic here
    return render(request, 'login.html')
def register(request):
    # Your view logic here
    return render(request, 'register.html')