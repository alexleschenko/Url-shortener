#coding=utf-8
from random import choice

from django.shortcuts import render, redirect

from forms import *
from models import *


# Create your views here.
def shortener(request):
    if request.method == 'POST':
        form = URL_create(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            url = ""
            url_list = Url.objects.filter().values('short_url')
            while url == "" or url in url_list: #генерация номера
                url = "http://127.0.0.1:8000/?shr="
                for i in range(6):
                    url += choice('1234567890abcdef')
            Url.objects.create(url=data['url'],short_url=url)
            data = Url.objects.filter().last()
            context = {'data': data}
            return render(request, 'done.html', context)
        context = {'my_form': form}
        return render(request, 'my_form.html', context)
    elif request.method == 'GET':
        if request.GET.items():
            shr = request.GET.get('shr') #счетчик кликов и переход по URL
            data = Url.objects.filter(short_url__icontains=shr).get()
            Url.objects.filter(short_url__icontains=shr).update(clicks=data.clicks + 1)
            return redirect(data.url)
        else:
            context = {'my_form': URL_create()}
            return render(request, 'my_form.html', context)


def url_list(request):
    data = Url.objects.filter()
    context = {'data': data}
    return render(request, 'list.html', context)
