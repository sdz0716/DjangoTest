from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
# Create your views here.

from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__contains=q)
        # message = 'You searched for: %r' % request.GET['q']
        return render_to_response('search_results.html', {'books': books, 'query': q})
    else:
        # message = 'You submitted an empty form.'    #对于用户提交过来的数据，甚至是正确的数据，都需要进行过滤。 在这里若没有进行检测，那么用户提交一个空的表单将引发KeyError异常。
    # return HttpResponse(message)
        return HttpResponse('Please submit a search term.')