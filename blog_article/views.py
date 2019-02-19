from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.http import JsonResponse
from django.core.paginator import Paginator

from unitls.all_form import CommentForm,WriteForm,BbsForm
from unitls.login_sugar import login_sugar
from unitls.make_uuid import make_uuid4

from blog_article.models import BlogArticle,Bbs
from likes.models import LikeUser
from blog_user.models import BlogUser
from read_num.models import ReadNum,AllReadNum
from comment.models import Comment

from config.config import article_page,bbs_page

# Create your views here.



def article(request,aid,page_num):
    '''文章页面'''
    obj = BlogArticle.objects.get(id=aid)
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" %(ct.model,obj.pk)
    # 是否点赞了这篇文章
    try:
        user_name = request.session['user_name']
        user_obj = BlogUser.objects.get(user_name=user_name)
        LikeUser.objects.get(content_type=ct, object_id=obj.pk, user=user_obj)
        like_status = True
    except:
        like_status = False

    date = timezone.now().date()
    # 单个文章计数
    readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
    # 总阅读数
    all_read_obj, all_created = AllReadNum.objects.get_or_create(all_date=date)
    if not request.COOKIES.get(key):
        readnum.read_num += 1
        readnum.save()
        all_read_obj.all_read_num += 1
        all_read_obj.save()

    comment_form = CommentForm(initial={'content_type':ct.model,'object_id':aid})
    comment_list = Comment.objects.filter(content_type=ct, object_id=aid)
    comment_list, all_page_num, article_num, has_pre, has_next, page_range = fenye(comment_list, page_num)
    response = render(request, 'blog_article.html', {'obj': obj,
                                                     'comment_form':comment_form,
                                                     'comment_list':comment_list,
                                                     'like_status':like_status,
                                                     'aid':aid,
                                                     'all_page_num': all_page_num,
                                                     'article_num': article_num,
                                                     'page_num': page_num,
                                                     'page_range': page_range,
                                                     'has_pre': has_pre,
                                                     'has_next': has_next,
                                                     })
    response.set_cookie(key,'true',max_age=600)
    return response

@login_sugar
def write_page(request):
    '''写文章页面'''
    write_form = WriteForm()
    if request.method == 'GET':
        obj = BlogArticle.objects.get(id=1)
        return render(request,'write_page.html',{'article':obj,'write_form':write_form})
    else:
        title = request.POST.get('title')
        content = request.POST.get('blog_text')
        type = request.POST.get('type')
        private = request.POST.get('private', 0)

        user_name = request.session['user_name']
        user_obj = BlogUser.objects.get(user_name=user_name)
        try:
            BlogArticle.objects.create(article_uuid=make_uuid4(),article_title=title, content=content, article_type=type, private=private,user=user_obj)
            data = {'res': 'sucess'}
        except:
            data = {'res': 'error', 'msg': '程序错误'}
        return JsonResponse(data)


def article_list(request,a_type,page_num):
    '''文章列表页面'''
    if a_type != 'ALL':
        all_obj = BlogArticle.objects.filter(article_type=a_type,private=False).order_by('-create_time',)
    else:
        all_obj = BlogArticle.objects.filter(private=False).order_by('-create_time',)

    obj_list, all_page_num, article_num, has_pre, has_next, page_range = fenye(all_obj, page_num)
    return render(request, 'article_list.html', {'obj_list': obj_list,
                                                 'a_type':a_type,
                                                 'all_page_num':all_page_num,
                                                 'article_num':article_num,
                                                 'page_num':page_num,
                                                 'page_range':page_range,
                                                 'has_pre':has_pre,
                                                 'has_next':has_next,
                                                 })


def bbs(request,page_num):
    bbs_input = BbsForm()
    obj_list = Bbs.objects.all().order_by('create_time', )

    bbs_list,all_page_num,bbs_num,has_pre,has_next,page_range = fenye(obj_list,page_num)
    return render(request,'bbs.html',{
        'bbs_input':bbs_input,
        'bbs_list':bbs_list,
        'all_page_num': all_page_num,
        'bbs_num': bbs_num,
        'page_num': page_num,
        'page_range': page_range,
        'has_pre': has_pre,
        'has_next': has_next,
    })


def bbs_sub(request):
    user_name = request.session['user_name']
    user_obj = BlogUser.objects.get(user_name=user_name)
    bbs_text = request.POST.get('bbs_text')
    if bbs_text:
        Bbs.objects.create(text=bbs_text, user=user_obj)
    return redirect('/blog_article/bbs/1.html')


def fenye(obj,page_num):
    paginator = Paginator(obj, bbs_page)
    obj_list = paginator.page(page_num)
    all_page_num = paginator.num_pages
    text_num = paginator.count
    has_pre = paginator.page(page_num).has_previous()
    has_next = paginator.page(page_num).has_next()
    if all_page_num < 5:
        page_range = paginator.page_range
    else:
        if page_num >= list(paginator.page_range)[-3]:
            page_range = list(paginator.page_range)[-5:]
            print(list(page_range))
        elif page_num <= list(paginator.page_range)[2]:
            page_range = list(paginator.page_range)[:5]
        else:
            page_range = list(paginator.page_range)[page_num - 3:page_num + 2]
    return obj_list,all_page_num,text_num,has_pre,has_next,page_range


# def bbs(request):
#     if request.method == 'GET':
#         bbs_input = BbsForm()
#         bbs_list = Bbs.objects.all().order_by('create_time', )
#         return render(request,'bbs.html',{'bbs_input':bbs_input,'bbs_list':bbs_list})
#     else:
#         user_name = request.session['user_name']
#         user_obj = BlogUser.objects.get(user_name=user_name)
#         bbs_text = request.POST.get('bbs_text')
#         try:
#             Bbs.objects.create(text=bbs_text,user=user_obj)
#             data = {'res': 'sucess'}
#         except:
#             data = {'res': 'error', 'msg': '程序错误'}
#         return JsonResponse(data)