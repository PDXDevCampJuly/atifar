from django.shortcuts import render


def javapic_query(request):
    return render(request, 'jumbotron.html')


def join_query(request):
    return render(request, 'join.html')


def gallery_query(request):
    return render(request, 'gallery.html')
