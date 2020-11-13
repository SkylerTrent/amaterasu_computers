from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_giveaway, name='giveaway'),
    path('add_vote/<give_away_item_id>/', views.add_vote, name='add_vote'),
]
