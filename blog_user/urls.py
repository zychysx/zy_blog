from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('send_check_num/',views.send_check_num),
    path('del_num/',views.del_num),
    path('is_name_valid/',views.is_name_valid),
    path('login_page.html',views.login_page),
    path('register.html',views.register_page),

    # path('test/',views.test),
    path('',views.index),
]