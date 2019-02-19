from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

# Create your models here.


class ReadNum(models.Model):
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')


# class OneReadNum(models.Model):
#     read_num = models.IntegerField(default=0)
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')


class AllReadNum(models.Model):
    all_date = models.DateField(default=timezone.now)
    all_read_num = models.IntegerField(default=0)