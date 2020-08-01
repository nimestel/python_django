from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog import settings


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html', context={
        'email': '123@mail.ru',
        'phone': '123456789',
        'server_time': datetime.now(),
    })


posts_data = [
    {
        'id': 0,
        'title': 'title 0',
        'date': datetime.now(),
        'text': """ some test0 """,
    },
    {
        'id': 1,
        'title': 'title 1',
        'date': datetime.now(),
        'text': """ some test1 """,
    },
    {
        'id': 2,
        'title': 'title 2',
        'date': datetime.now(),
        'text': """ some test2 """,
    },
    {
        'id': 3,
        'title': 'The Zen of Python, by Tim Peters',
        'date': datetime.now(),
        'text': """<i>Beautiful is better than ugly.<br>
Explicit is better than implicit.<br>
Simple is better than complex.<br>
Complex is better than complicated.<br>
Flat is better than nested.<br>
Sparse is better than dense.<br>
Readability counts.<br>
Special cases aren't special enough to break the rules.<br>
Although practicality beats purity.<br>
Errors should never pass silently.<br>
Unless explicitly silenced.<br>
In the face of ambiguity, refuse the temptation to guess.<br>
There should be one-- and preferably only one --obvious way to do it.<br>
Although that way may not be obvious at first unless you're Dutch.<br>
Now is better than never.<br>
Although never is often better than *right* now.<br>
If the implementation is hard to explain, it's a bad idea.<br>
If the implementation is easy to explain, it may be a good idea.<br>
Namespaces are one honking great idea -- let's do more of those!</i>"""
    }
]


def posts(request):
    return render(request, 'posts.html', context={
        'posts': reversed(posts_data)
    })


def post(request, number):
    if number >= len(posts_data):
        return redirect('/posts')
    return render(request, 'post.html', context=posts_data[number])


def publish(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')

        if not password or not title or not text:
            return render(request, 'publish.html', {'error': 'empty field!'})
        if password != settings.PUBLISH_PASSWORD:
            return render(request, 'publish.html',  {'error': 'invalid password!'})

        posts_data.append({
            'id': len(posts_data),
            'title': title,
            'date': datetime.now(),
            'text': text
        })
        return redirect('/posts/' + str(posts_data[-1]['id']))

    return render(request, 'publish.html')
