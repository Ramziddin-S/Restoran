from django.shortcuts import render


def home_page(request):
    return render(request, 'dishes/index.html')


def about(request):
    return render(request, 'dishes/about.html')


def menu(request):
    return render(request, 'dishes/menu.html')