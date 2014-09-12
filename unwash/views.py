from django.shortcuts import render


def salon(request):
    ctx = {}

    return render(request, 'unwash/salon.html', ctx)
