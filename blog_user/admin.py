from django.contrib import admin
from .models import BlogUser
# Register your models here.


@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    list_display = ['user_name','n_name','password','email','write_key','super_key','comment_key','cerate_time','update_time']
    search_fields = ['user_name','n_name','email']

    date_hierarchy = 'cerate_time'
    # list_filter = ('',)
