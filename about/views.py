from django.shortcuts import render, redirect
from .models import About, CollaborateRequest
from django.contrib import messages

# Create your views here.
def about(request):

    if request.method == "POST":
        form = CollaborateRequest(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request sent successfully!")
            return redirect('about')
        else:
            messages.add_message(request, messages.ERROR, "Error sending collaboration request. Please try again.")

    about = About.objects.all().order_by("-updated_on").first()
    form = CollaborateRequest()
    
    return render(request, 'about/about.html', {
        'about': about,
        'form': form,
    })
