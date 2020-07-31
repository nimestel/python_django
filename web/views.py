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


def posts(request):
    return render(request, 'posts.html', context={
        'posts': [
            {'name': 'post1', 'date': 123},
            {'name': 'post2', 'date': 321},
        ],
    })


def post(request):
    return render(request, 'post.html', context={
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
    })
