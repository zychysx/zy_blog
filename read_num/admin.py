from django.contrib import admin
from .models import ReadNum,AllReadNum

# Register your models here.

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ['date','read_num','object_id','content_object']
    search_fields = ['date', ]

    date_hierarchy = 'date'
    list_filter = ('date',)


@admin.register(AllReadNum)
class AllReadNumAdmin(admin.ModelAdmin):
    list_display = ['all_date','all_read_num']
    search_fields = ['all_date', ]

    date_hierarchy = 'all_date'
    list_filter = ('all_date',)