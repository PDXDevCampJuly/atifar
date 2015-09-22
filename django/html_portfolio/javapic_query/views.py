from django.shortcuts import render


def javapic_query(request):
    return render(request, 'jumbotron_query.html')


def join_query(request):
    return render(request, 'join_query.html')


def gallery_query(request):
    return render(request, 'gallery_query.html')
