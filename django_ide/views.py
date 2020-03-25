from django.http import HttpResponse


def index(request):
    return HttpResponse('OK!')


def article(request, year):
    return HttpResponse('article: ' + year)

