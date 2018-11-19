from django.conf.urls import url
from . import views
from .views import JogoList
from django.urls import path

urlpatterns = [
    path('', views.JogoList.as_view()),  
    path('<int:pk>', views.JogoDetail.as_view()),
]
