from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Card
from .forms import CardForm
# from django.views.generic import ListView
# from django.contrib.auth.mixins import LoginRequiredMixin



# Home page view
def home(request):
    return render(request, 'chaos_app/home.html')

# Card list view
############################### Function-based view
@login_required
def user_cards_view(request):
    """
    Display a list of cards created by the logged-in user.
    The cards are ordered by the date they were created, in descending order.
    """
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect('user_cards')
    else:
        form = CardForm()

    user_cards = Card.objects.filter(user=request.user).order_by('-created_on')
    paginator = Paginator(user_cards, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'chaos_app/user_cards.html', {
        'form': form,
        'cards': page_obj,
        'is_paginated': paginator.num_pages > 1,
        'page_obj': page_obj,
    })



########################## Class-based view

# class UserCardsView(LoginRequiredMixin, ListView):
#     model = Card
#     template_name = 'chaos_app/user_cards.html'
#     context_object_name = 'cards'
#     paginate_by = 12

#     def get_queryset(self):
#         """
#         Return the list of cards created by the logged-in user,
#         ordered by the date they were created, in descending order.
#         """
#         return Card.objects.filter(user=self.request.user).order_by('-created_on')


