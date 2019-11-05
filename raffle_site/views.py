from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Participant, RaffleSession

def index(request):
    return render(request, 'raffle_site/index.html')

def raffle_setup_page(request, session_key):
    session = get_object_or_404(RaffleSession, pk=session_key)
    return render(request, 'raffle_site/setup.html', {'session': session})

def raffle_page(request, session_key):
    return HttpResponse(f"Raffle Page {session_key}")