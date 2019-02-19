from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from blog_user.models import BlogUser
# Create your models here.


class LikeCount(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    like_count = models.IntegerField(default=0)


class LikeUser(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(BlogUser,on_delete=models.DO_NOTHING)
    like_time = models.DateTimeField(auto_now_add=True)