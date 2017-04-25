from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
# Create your views here.

from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search_form.html')

def search_old(request):    #优化前
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__contains=q)
        # message = 'You searched for: %r' % request.GET['q']
        return render_to_response('search_results.html', {'books': books, 'query': q})
    else:
        # message = 'You submitted an empty form.'    #对于用户提交过来的数据，甚至是正确的数据，都需要进行过滤。 在这里若没有进行检测，那么用户提交一个空的表单将引发KeyError异常。
    # return HttpResponse(message)
    #     return HttpResponse('Please submit a search term.')
        return render_to_response('search_form.html', {'error': True})

def search(request):    #优化后，当用户访问/search/并未提交任何数据时就隐藏错误信息，这样就移去search_form()视图以及对应的URLpattern
    # error = False
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            # error = True
            error.append('Enter a search term.')
        elif len(q) > 20:
            # error =True
            error.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__contains=q)
            return render_to_response('search_results.html', {'books':books, 'query':q})
    return render_to_response('search_form.html', {'error': error})
#修改一，在改进后的视图中，若用户访问/search/并且没有带有GET数据，那么他将看到一个没有错误信息的表单； 如果用户提交了一个空表单，那么它将看到错误提示信息，还有表单； 最后，若用户提交了一个非空的值，那么他将看到搜索结果。
#修改二，提交一个空表单怎么会出现一个关于20个字符限制的提示会产生疑议。问题的实质在于我们只使用来一个布尔类型的变量来检测是否出错，而不是使用一个列表来记录相应的错误信息。
