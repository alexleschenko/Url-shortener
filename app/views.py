from django.shortcuts import render, redirect
import arrow
from forms import *
from models import *
from random import choice
from django.http import HttpResponse
# Create your views here.
def shortener(request):
    if request.method == 'POST':
        form = URL_create(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            time = arrow.utcnow()
            url = ""
            url_list = Url.objects.filter().values('short_url')
            while url == "" or url in url_list:
                url = ""
                for i in range(6):
                    url += choice('1234567890abcdef')
            Url.objects.create(url=data['url'], cr_time = time.format('YYYY - MM - DD HH:mm:ss'), short_url=url)
            return HttpResponse("You've been create short URL")
        context = {'my_form':form}
        return render(request, 'my_form.html', context)
    else:
        context = {'my_form':URL_create()}
        return render(request, 'my_form.html', context)