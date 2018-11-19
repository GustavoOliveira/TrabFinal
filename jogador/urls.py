from django.conf.urls import url
from . import views
from .views import JogadorList
from django.urls import path

urlpatterns = [
    path('', views.JogadorList.as_view(), name='file-upload'),  
    path('<int:pk>', views.JogadorDetail.as_view()),
]
