from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index_page, name='home-page'),
    # path ('header', views.header_comonent, name='header_component'),
    # path ('header', views.header_comonent, name='header_component'),



]