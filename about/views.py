from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("About page successfully wired up!")
