from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse,JsonResponse
from likes.models import LikeUser,LikeCount
from blog_article.models import BlogArticle
from blog_user.models import BlogUser
from unitls.login_sugar import ajax_login_sugar

# Create your views here.


@ajax_login_sugar
def like_btn_click(request,aid):
    user_name = request.session['user_name']
    user_obj = BlogUser.objects.get(user_name=user_name)

    obj = BlogArticle.objects.get(id=aid)
    ct = ContentType.objects.get_for_model(BlogArticle)

    like_user, user_created = LikeUser.objects.get_or_create(content_type=ct, object_id=obj.pk, user=user_obj)
    if user_created:
        like_count,like_created = LikeCount.objects.get_or_create(content_type=ct,object_id=obj.pk)
        like_count.like_count += 1
        like_count.save()
        like_status = True
    else:
        like_user.delete()
        like_count, like_created = LikeCount.objects.get_or_create(content_type=ct, object_id=obj.pk)
        like_count.like_count += -1
        like_count.save()
        like_status = False

    return JsonResponse({'like_count':like_count.like_count,'like_status':like_status})


