from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponse('OK!')


def article(request, year):
    url = reverse('article_detail', args=(year, ))
    return HttpResponse('article: ' + url + year)

