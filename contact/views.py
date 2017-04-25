from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def contact(request):
    error = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            error.append('Enter a subject')
        if not request.POST.get('message', ''):
            error.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            error.append('Enter a vaild e-mail address.')
        if not error:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html', {'error': error, 'subject': request.POST.get('subject', ''), 'message': request.POST.get('message', ''), 'email': request.POST.get('email', ''), })    #若用户刷新一个包含POST表单的页面，那么请求将会重新发送造成重复。 这通常会造成非期望的结果，比如说重复的数据库记录；在我们的例子中，将导致发送两封同样的邮件。 如果用户在POST表单之后被重定向至另外的页面，就不会造成重复的请求了。
#第一次优化，即'error':error后面的内容，可以若数据验证失败后，返回客户端的表单中各字段最好是填有原来提交的数据。