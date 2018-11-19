from django.conf.urls import url
from . import views
from .views import CampeonatoList
from django.urls import path

urlpatterns = [
    path('', views.CampeonatoList.as_view(), name='file-upload'),  
    path('<int:pk>', views.CampeonatoDetail.as_view()),
]
