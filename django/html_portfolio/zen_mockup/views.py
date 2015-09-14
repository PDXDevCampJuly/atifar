from django.shortcuts import render

def zen_mockup(request):
    return render(request, 'zen_mockup.html')
