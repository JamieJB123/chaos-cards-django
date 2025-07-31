from django.shortcuts import render

def index(request):
    return render(request, 'chaos_app/home.html')
