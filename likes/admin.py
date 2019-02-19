from django.contrib import admin
from likes.models import LikeCount,LikeUser
# Register your models here.

@admin.register(LikeCount)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ['like_count','object_id','content_object']


@admin.register(LikeUser)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ['user','like_time','object_id','content_object']
    search_fields = ['like_time','user' ]

    date_hierarchy = 'like_time'
    list_filter = ('like_time',)
