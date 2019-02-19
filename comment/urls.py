from django.urls import path
from . import views


urlpatterns =[
    path('arcticle_comment/',views.arcticle_comment),
]