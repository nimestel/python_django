from django.urls import path

from web import views

urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts),
    path('posts', views.posts),
    path('posts/<int:number>', views.post),
    path('publish', views.publish),
]
