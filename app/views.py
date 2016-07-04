from django.shortcuts import render, redirect
import arrow
from forms import *
from models import *
from random import choice
# Create your views here.
def shortener(request):
    if request.method == 'POST':
        form = URL_create(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            time = arrow.utcnow()
            list_url = [""]
            for i in Url.objects.filter().values('short_utl'):
                list_url.append(i[-6:])
            url_sh = ""
            while url_sh in list_url:
                url_sh=""
                for i in range(6):
                    url_sh += choice('1234567890abcdef')
            Url.objects.create(url=data['url'], cr_time = time.format('YYYY - MM - DD HH:mm:ss'), short_url=url_sh)
            data = Url.objects.filter().last()
            context = {'data':data}
            return render(request, 'create_url', context)