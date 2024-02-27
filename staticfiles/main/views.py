from django.shortcuts import render

def index(request):
    print('rendering index.html')
    return render(request, 'index.html')