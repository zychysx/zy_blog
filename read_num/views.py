from django.shortcuts import render
from .models import ReadNum,AllReadNum
from blog_article.models import BlogArticle
from django.utils import timezone
from django.http import HttpResponse,JsonResponse
import datetime
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def all_read_num_chart(request):
    today = timezone.now().date()
    date_list = []
    num_list = []
    for i in range(6,-1,-1):
        date = today - datetime.timedelta(days=i)
        date_list.append(date)
        try:
            all_obj = AllReadNum.objects.get(all_date=date)
            num_list.append(all_obj.all_read_num)
        except :
            num_list.append(0)
    return JsonResponse({
        'date_list':date_list,
        'num_list':num_list,
    })


def read_num_chart(request,id):
    today = timezone.now().date()
    date_list = []
    num_list = []
    obj = BlogArticle.objects.get(id=id)
    ct = ContentType.objects.get_for_model(BlogArticle)
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        date_list.append(date)
        try:
            read_num_obj = ReadNum.objects.get(content_type=ct, object_id=obj.pk, date=date)
            num_list.append(read_num_obj.read_num)
        except :
            num_list.append(0)
    return JsonResponse({
        'date_list': date_list,
        'num_list': num_list,
    })
