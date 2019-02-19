from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType

from comment.models import Comment
from blog_user.models import BlogUser
from unitls.login_sugar import login_sugar

# Create your views here.


@login_sugar
def arcticle_comment(request):
    content_type = request.POST.get('content_type')
    object_id = request.POST.get('object_id')
    text = request.POST.get('commen_text')
    user_name = request.session['user_name']
    user = BlogUser.objects.get(user_name=user_name)

    model_class = ContentType.objects.get(model=content_type).model_class()
    model_obj = model_class.objects.get(pk=object_id)

    if  not text.replace(' ',''):
        return JsonResponse({'res':'error','msg':'评论内容不能为空'})
    try:
        Comment.objects.create(
            content_object = model_obj,
            text=text,
            user=user
    )
        data = {'res':'sucess'}
    except:
        data = {'res':'error','msg':'程序错误'}

    return  JsonResponse(data)