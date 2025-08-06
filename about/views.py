from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import FeedbackForm


# Create your views here.
def about(request):

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Contact form sent successfully!")
            return redirect('about')
        else:
            messages.add_message(request, messages.ERROR, "Error sending contact form. Please try again.")

    about = About.objects.all().order_by("-updated_on").first()
    form = FeedbackForm()

    return render(request, 'about/about.html', {
        'about': about,
        'form': form,
    })
