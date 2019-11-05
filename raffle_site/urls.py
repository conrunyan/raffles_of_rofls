from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setup/<slug:session_key>', views.raffle_setup_page, name='setup'),
    path('raffle/<slug:session_key>', views.raffle_page, name='raffle'),

]
