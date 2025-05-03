from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from clubs.forms import AddArticleForm


def index(request):
    context = {
        'title': 'ГОЛОВНА',
        'content': "Європейські клуби",
    }

    return render(request, 'clubs/index.html', context)


def articles(request):
    return render(request, 'clubs/articles.html')


def add_article(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = AddArticleForm()

    context = {'add_article': 'Додати статтю',
               'form': form,
               }
    return render(request, 'clubs/add_article.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Куди ти заліз! Немає такої сторінки!</h1>")
