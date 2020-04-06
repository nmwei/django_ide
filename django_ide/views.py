from django.http import HttpResponse
from django.urls import reverse


def index(request):
    url = reverse('article_detail', args=(2020,))
    url_auth = reverse('auth:index')
    print(url_auth)
    return HttpResponse('OK!' + url)


def article(request, year):
    url = reverse('article_detail', args=(year, ))
    return HttpResponse('article: ' + url + year)

