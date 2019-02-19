from django.shortcuts import redirect
from django.http import JsonResponse

def login_sugar(func):
    def wapper(request,*args,**kwargs):
        if request.session.get('is_login',False):
            return func(request,*args,**kwargs)
        else:
            return redirect('/blog_user/login_page.html')
    return wapper


def ajax_login_sugar(func):
    def ajax_wapper(request,*args,**kwargs):
        if request.session.get('is_login',False):
            return func(request,*args,**kwargs)
        else:
            return JsonResponse({
                'next_path':'/blog_user/login_page.html'
            })
    return ajax_wapper