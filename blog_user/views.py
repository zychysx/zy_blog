from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from blog_user.tasks import *

from blog_article.models import BlogArticle
from blog_user.models import BlogUser
from read_num.models import ReadNum

from unitls.random_num import ran_num
from unitls.make_uuid import make_uuid4

# Create your views here.


def index(request):
    '''首页'''
    # obj_list=BlogArticle.objects.all().order_by('-create_time',)[:5]
    obj_list = BlogArticle.objects.filter(private=False).order_by('-create_time',)[:5]
    return render(request,'index.html',{'obj_list':obj_list})


def register_page(request):
    return render(request, 'register.html')

def register(request):
    user_name = request.POST.get('user_name')
    password = request.POST.get('pass_word')
    email = request.POST.get('user_email')
    n_name = request.POST.get('n_name')
    check_num = request.POST.get('check_num')
    if request.session[email] == int(check_num):
        obj,created = BlogUser.objects.get_or_create(user_uuid=make_uuid4(),user_name=user_name,password=password,email=email,n_name=n_name)
        request.session['user_name'] = obj.user_name
        request.session['n_name'] = obj.n_name
        request.session['user_uuid'] = obj.user_uuid
        request.session['is_login'] = True
        if obj.super_key:
            request.session['super_key'] = obj.super_key
        if obj.private_key:
            request.session['private_key'] = obj.private_key
        if obj.write_key:
            request.session['write_key'] = obj.write_key

        # send_user_mail.delay(email)
        send_user_mail_thread = SendUserMailThread(email)
        send_user_mail_thread.start()
        return redirect(request.session.get('pre_path', '/'))
    else:
        return HttpResponse('验证码错误')


def login_page(request):
    return render(request,'login.html')


def login(request):
    user_name = request.POST.get('user_name')
    password = request.POST.get('pass_word')

    obj = BlogUser.objects.get(user_name=user_name)
    if obj.password == password:
        request.session['is_login'] = True
        request.session['user_name'] = obj.user_name
        request.session['n_name'] = obj.n_name
        request.session['user_uuid'] = obj.user_uuid
        if obj.super_key:
            request.session['super_key'] = obj.super_key
        if obj.private_key:
            request.session['private_key'] = obj.private_key
        if obj.write_key:
            request.session['write_key'] = obj.write_key

        next = request.session.get('pre_path','/')
        data = {
            'res':1,
            'next_path':next
        }
        return JsonResponse(data)
    else:
        return JsonResponse({
            'login_error_msg':'用户名或密码错误'
        })

def logout(request):
    next = request.session.get('pre_path', '/')
    try:
        del request.session['n_name']
        del request.session['user_name']
        del request.session['user_uuid']
        del request.session['is_login']
        try:
            del request.session['super_key']
        except:
            pass
        try:
            del request.session['private_key']
        except:
            pass
        try:
            del request.session['write_key']
        except:
            pass
        return redirect(next)
    except:
        return redirect(next)

'''
def send_check_num(request):
    # celery
    email = request.GET.get('user_email')
    ran_n = ran_num()
    request.session[email] = ran_n
    send_num.delay(email,str(ran_n))
    data = {'res':'success'}
    return JsonResponse(data)
'''


def send_check_num(request):
    # thread
    email = request.GET.get('user_email')
    ran_n = ran_num()
    request.session[email] = ran_n
    send_num_thread = SendNumThread(email,str(ran_n))
    send_num_thread.start()
    data = {'res':'success'}
    return JsonResponse(data)

def del_num(request):
    '''删除过期验证码'''
    email = request.GET.get('user_email')
    del request.session[email]
    data = {'res':'success'}
    return JsonResponse(data)

def is_name_valid(request):
    '''校验用户名是否存在'''
    user_name = request.GET.get('user_name')
    if BlogUser.objects.filter(user_name=user_name).exists():
        return JsonResponse({'res': '0'})
    else:
        return JsonResponse({'res': '1'})