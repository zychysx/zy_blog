from django.contrib import admin
from blog_article.models import BlogArticle,Bbs
# Register your models here.


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ['id','article_title','article_type','read_num','lick_count','comment_count','create_time','update_time']
    search_fields = ['article_title',]

    date_hierarchy = 'create_time'
    list_filter = ('article_type',)


@admin.register(Bbs)
class BbsAdmin(admin.ModelAdmin):
    list_display = ['id','user','create_time',]
    date_hierarchy = 'create_time'
    search_fields = ['user', ]