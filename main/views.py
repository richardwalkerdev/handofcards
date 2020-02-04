from django.shortcuts import render
import requests
import os
from django.core.exceptions import ImproperlyConfigured
from .models import Hand
import datetime


def hand(request):

    def get_env_value(env_variable):
        try:
            return os.environ[env_variable]
        except KeyError:
            error_msg = 'Set the {} environment variable'.format(env_variable)
            raise ImproperlyConfigured(error_msg)

    # Get environmant variable DECKOFCARDS_URL
    DECKOFCARDS_URL = get_env_value('DECKOFCARDS_URL')

    response = requests.get(DECKOFCARDS_URL)
    deckdata = response.json()
 
    hand = []
    total = 0

    for n in range(2):
        hand.append(deckdata.pop(0))

    for i in hand:
        total = total + i.get("value")

    handTotal = Hand()
    handTotal.total = total
    handTotal.created = datetime.datetime.now()
    handTotal.save()

    return render(request, 'main/index.html', {'array': hand, 'total': total})