from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request) -> HttpResponse:
    return HttpResponse('Добро пожаловать в WatchShop!')


def about(request) -> HttpResponse:
    return render(request, 'other/about.html')


def pagesNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс! Такой страницы нет</H1>')  # функция для генерации исключения


handler404 = pagesNotFound
