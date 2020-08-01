from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from web.models import Post
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
    post_objects = Post.objects.all()
    return render(request, 'posts.html', context={
        'posts': post_objects
    })


def post(request, number):
    try:
        post = Post.objects.get(id=number)
    except Post.DoesNotExist:
        return redirect('/posts')
    return render(request, 'post.html', context={
        'post': post
    })


def publish(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')

        if not password or not title or not text:
            return render(request, 'publish.html', {'error': 'empty field!'})
        if password != settings.PUBLISH_PASSWORD:
            return render(request, 'publish.html',  {'error': 'invalid password!'})

        post = Post(text=text, title=title)
        post.save()
        return redirect('/posts/' + str(post.id))

    return render(request, 'publish.html')
