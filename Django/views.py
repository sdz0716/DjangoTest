from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse('hello world')

#方法一
# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = '<html><body>It is now %s.</html></body>' % now
#     return HttpResponse(html)

#方法二
# def current_datetime(request):
#     now = datetime.datetime.now()
#     # tem = Template('<html><body>It is now {{ var }}.</html></body>')
#     tem = get_template('current_datetime.html')
#     html = tem.render({'var': now})
#     # html = tem.render(Context({'var': now}))  使用get_template方法时，render不接受Context(上下文)类型，只接受dict。如在试图里直接写html，则需要在render中使用Context()。
#     return HttpResponse(html)

#方法三
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'var': now})    #render_to_response() 返回 HttpResponse 对象。第一个参数必须是要使用的模板名称。 如果要给定第二个参数，那么该参数必须是为该模板创建 Context 时所使用的字典。 如果不提供第二个参数， render_to_response() 使用一个空字典。

def hours_ahead(request, offset):
    try:
        offset = int(offset)    #捕获值永远都是字符串（string）类型，而不会是整数（integer）类型
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = '<html><body>In %s hour(s), it will be %s.</body></html>' % (offset, dt)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})