from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Card


# Home page view
def home(request):
    return render(request, 'chaos_app/home.html')

# Card list view

class UserCardsView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'chaos_app/user_cards.html'
    context_object_name = 'cards'
    paginate_by = 12 

    def get_queryset(self):
        """
        Return the list of cards created by the logged-in user,
        ordered by the date they were created, in descending order.
        """
        return Card.objects.filter(user=self.request.user).order_by('-created_on')
