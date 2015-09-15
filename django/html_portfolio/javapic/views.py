from django.shortcuts import render


def javapic(request):
    return render(request, 'jumbotron.html')


def join(request):
    return render(request, 'join.html')


def gallery(request):
    return render(request, 'gallery.html')
