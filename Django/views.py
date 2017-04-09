from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse('hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s' % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)    #捕获值永远都是字符串（string）类型，而不会是整数（integer）类型
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hour(s), it will be %s.</body></html>' % (offset, dt)
    return HttpResponse(html)