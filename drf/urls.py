from django.urls import path
from . import views

urlpatterns = [

    path('',views.PaperApiView.as_view()),
    path('<pk>',views.PaperDetailApiView.as_view()),
    path('authors/',views.AuthorApiView.as_view()),
    path('authors/<pk>',views.AuthorDetailApiView.as_view())

]