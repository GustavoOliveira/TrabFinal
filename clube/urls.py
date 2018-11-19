from django.conf.urls import url
from . import views
from .views import ClubeList
from django.urls import path

urlpatterns = [
    path('', views.ClubeList.as_view(), name='file-upload'),  
    path('<int:pk>', views.ClubeDetail.as_view()),
]
