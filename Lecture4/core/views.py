from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render


def current_time(request):
    return HttpResponse(str(datetime.now()))


def time_plus(request):
    if request.GET['hours']:
        dt = datetime.now() + timedelta(hours=int(request.GET['hours']))
        return HttpResponse(dt)
    return HttpResponse('null')


def hours_ahead(request, **kwargs):
    dt = datetime.now() + timedelta(hours=kwargs.get('hours'), days=kwargs.get('days'))
    return HttpResponse(dt)
