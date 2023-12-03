from django.urls import path
from . import views

urlpatterns = [
    path ('', views.paper_list, name='paper-list'),
    path('<slug:slug>', views.paper_detail, name='paper-detail'),


]