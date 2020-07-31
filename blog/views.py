from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>My blog</h1>'
                        '<p>Hello, World!</p>'
                        '<a href="/contacts">Contacts</a><br>'
                        '<a href="/articles">Articles</a>')


def contacts(request):
    return HttpResponse('<h2>My contacts</h2>'
                        '<p>email: 123@mail.ru</p>'
                        '<a href="/">Go back</a>')


def articles(request):
    return HttpResponse('<p>100 posts!</p>'
                        '<a href="/">Go back</a>')
