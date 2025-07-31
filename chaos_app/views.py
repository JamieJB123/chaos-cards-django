from django.shortcuts import render

def home(request):
    return render(request, 'chaos_app/home.html')
