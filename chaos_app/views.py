import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Card
from .forms import CardForm
# from django.views.generic import ListView
# from django.contrib.auth.mixins import LoginRequiredMixin



# Home page view
def home(request):
    """Render the home page of the application.
    Home view differs depending on authentication status:
    - If the user is authenticated, see a basic home page with option to play the game.
    - If the user is not authenticated, they see a more descriptive home page with option to register or log-in.
    This is handled in the template.
    """
    return render(request, 'chaos_app/home.html', {
        'spin_attempted': False,  # Flag to indicate if the spin button has been pressed
    })

#Random Card Generator View
@login_required
def random_card_view(request):
    """
    Display a random card from the user's collection.
    If the user has no cards, display a message indicating that.
    """
    user_cards = Card.objects.filter(user=request.user)
    print(f'User cards: {user_cards}')
    print(f'Cards exist: {user_cards.exists()}')
    if user_cards.exists():
        random_card = random.choice(user_cards)  # Select a random card if cards exist
        spin_attempted = True # Set a flag to indicate that a spin was attempted
    else:
        random_card = None  # Set to None if no cards exist
        spin_attempted = True # Still set the flag to indicate a spin was attempted

    return render(request, 'chaos_app/home.html', {
        'random_card': random_card,
        'spin_attempted': spin_attempted,  # Pass the flag to the template
    })

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
            messages.add_message(request, messages.SUCCESS, 'Card created successfully!')
            return redirect('user_cards')
        else:
            messages.add_message(request, messages.ERROR, 'Error creating card. Please try again.')
    else:
        form = CardForm()

    user_cards = Card.objects.filter(user=request.user).order_by('-created_on')
    paginator = Paginator(user_cards, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'chaos_app/user_cards.html', {
        'form': form,
        'cards': page_obj,
        'is_paginated': paginator.num_pages > 1,
        'page_obj': page_obj,
    })

def edit_card_view(request, card_id):
    """
    Edit an existing card created by the logged-in user.

    """
    if request.method == "POST":
        card = Card.objects.get(id=card_id, user=request.user)
        form = CardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            messages.add_message(request, messages.SUCCESS, "Card updated successfully!")
            return redirect('user_cards')
        else:
            messages.add_message(request, messages.ERROR, "Error updating card. Please try again.")
    return redirect('user_cards')

def delete_card_view(request, card_id):
    """
    Delete an existing card created by the logged-in user.
    """
    card = Card.objects.get(id=card_id, user=request.user)
    if card:
        card.delete()
        messages.add_message(request, messages.SUCCESS, "Card deleted successfully!")
    else:
        messages.add_message(request, messages.ERROR, "Error deleting card. Card not found.")
    return redirect("user_cards")

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


