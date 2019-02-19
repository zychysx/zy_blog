from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from django.db.models.aggregates import Sum,Count

from read_num.models import ReadNum
from likes.models import LikeCount
from comment.models import Comment
from blog_user.models import BlogUser

# Create your models here.

ARTICLE_TYPE = (
    ('D','美食'),
    ('W','网站搭建'),
    ('T','游记'),
    ('TR','琐事'),
    ('DJ','Django'),
    ('P','Python'),
)



class BlogArticle(models.Model):
    article_uuid = models.CharField(max_length=100)
    user = models.ForeignKey('blog_user.BlogUser',on_delete=models.CASCADE,default=1)
    article_title = models.CharField(max_length=300)
    article_type = models.CharField(max_length=10,choices=ARTICLE_TYPE)
    content = RichTextField()
    private = models.BooleanField(default=False)
    recommend = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

    def read_num(self):
        ct = ContentType.objects.get_for_model(self)
        readnum=ReadNum.objects.filter(content_type=ct, object_id=self.pk).aggregate(readnum=Sum('read_num'))
        return readnum['readnum']

    def lick_count(self):
        ct = ContentType.objects.get_for_model(self)
        try:
            like_obj = LikeCount.objects.get(content_type=ct, object_id=self.pk)
            return like_obj.like_count
        except:
            return 0

    def comment_count(self):
        ct = ContentType.objects.get_for_model(self)
        comment_num = Comment.objects.filter(content_type=ct, object_id=self.pk).aggregate(comment_num=Count('text'))
        return comment_num['comment_num']

    def __str__(self):
        return self.article_title


    class Meta:
        db_table = 'blogarticle'


class Bbs(models.Model):
    text = RichTextField()
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(BlogUser, on_delete=models.DO_NOTHING)