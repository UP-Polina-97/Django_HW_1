import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f'Текущее время:'
    html = f"<html><body> {msg} %s. </body></html>" % current_time
    return HttpResponse(html)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    path = os.path.abspath(os.getcwd())
    directory_list = os.listdir(path)
    msg = "<h1 style='color: green'>Содержимое рабочей директории</h1>"      #'Содержимое рабочей директории'
    html = f"<html><body> {msg} %s. </body></html>" % directory_list
    return HttpResponse(html)


