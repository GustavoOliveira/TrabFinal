from django.conf.urls import url
from . import views
from .views import OrganizadorList
from django.urls import path

urlpatterns = [
    path('', views.OrganizadorList.as_view(), name='file-upload'),  
    path('<int:pk>', views.OrganizadorDetail.as_view()),
]
