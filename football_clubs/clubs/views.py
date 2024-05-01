from django.shortcuts import render


def index(request):
    context = {
        'title': 'ГОЛОВНА',
        'content': "Європейські клуби",
    }

    return render(request, 'clubs/index.html', context)
