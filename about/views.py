from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("About page successfully wired up!")
