from django.urls import path
from likes import views

urlpatterns = [
    path('like_btn/<int:aid>/', views.like_btn_click),
]