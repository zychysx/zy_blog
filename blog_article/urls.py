from django.urls import path
from blog_article import views



urlpatterns = [
    path('article/<int:aid>/<int:page_num>.html',views.article),
    path('write_page.html',views.write_page),
    path('sub_article/',views.write_page),
    path('article_list/<str:a_type>/<int:page_num>.html',views.article_list),
    path('bbs/<int:page_num>.html',views.bbs),
    path('bbs_sub/',views.bbs_sub),

]