from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html', context={
        'email': '123@mail.ru',
        'phone': '123456789',
        'server_time': datetime.now(),
    })


def articles(request):
    return render(request, 'articles.html', context={
        'posts': [
            {'name': 'post1', 'date': 123},
            {'name': 'post2', 'date': 321},
        ],
    })
