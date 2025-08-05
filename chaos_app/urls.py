# filepath: chaos_app/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-cards/', views.user_cards_view, name='user_cards'),
    path('spin/', views.random_card_view, name='spin_card'),
]
