from django.shortcuts import render
#configurando la vista recien
#creada
def home(request):
    return render(request, 'home.html')
