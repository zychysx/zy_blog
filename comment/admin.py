from django.contrib import admin
from comment.models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','content_object','comment_time','text']
    list_filter = ('comment_time',)