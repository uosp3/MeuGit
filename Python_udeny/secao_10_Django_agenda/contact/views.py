from django.shortcuts import render


def index(request):
    return render(
        request,
        'contact/index.html',  # o que será renderizado
    )
