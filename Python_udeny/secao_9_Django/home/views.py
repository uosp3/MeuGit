from django.shortcuts import render


def home(request):
    print('home')

    context = {
            'text': 'Olá home'  # isso vai para o index.html
        }

    return render(
        request,
        'home/index.html',
        context,
    )
