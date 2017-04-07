from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse('hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s' % now
    return HttpResponse(html)

def hours_ahead(request):
