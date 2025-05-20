from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from clubs.forms import AddArticleForm
from clubs.models import Articles


def index(request):
    context = {
        'title': 'ГОЛОВНА',
        'content': "Європейські клуби",
    }

    return render(request, 'clubs/index.html', context)


def article(request):
    articles = Articles.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'clubs/article.html', context)


@login_required
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


def show_article(request, article_slug):
    article = get_object_or_404(Articles, slug=article_slug)

    context = {
        'article': article,
    }
    return render(request, 'clubs/show_article.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Куди ти заліз! Немає такої сторінки!</h1>")
