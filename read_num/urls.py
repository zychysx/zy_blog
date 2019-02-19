from django.urls import path
from read_num import views


urlpatterns = [
    path('all_read_num/',views.all_read_num_chart),
    path('read_num/<int:id>/',views.read_num_chart),
]