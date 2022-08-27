from django.shortcuts import render

# Create your views here.


def authView(request):
    return render(request, 'google.html',{})