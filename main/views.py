from django.shortcuts import render
import requests


def hand(request):

    response = requests.get('http://127.0.0.1:7000/deck/')
    deckdata = response.json()
  
    hand = []
    total = 0

    for n in range(2):
        hand.append(deckdata.pop(0))

    for i in hand:
        total = total + i.get("value")

    return render(request, 'main/index.html', {'array': hand, 'total': total})
