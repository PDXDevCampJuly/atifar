from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf


def javapic(request):
    return render(request, 'jumbotron.html')


def join(request):
    return render(request, 'join.html')


def gallery(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('gallery.html', c)