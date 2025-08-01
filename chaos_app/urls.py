# filepath: chaos_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-cards/', views.UserCardsView.as_view(), name='user_cards'),
]
