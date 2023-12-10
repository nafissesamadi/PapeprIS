from django.urls import path
from . import views

urlpatterns = [
    # path ('', views.paper_list, name='paper-list'),
    path('', views.PaperListView.as_view(), name='paper-list'),
    # path ('<slug:slug>', views.paper_detail, name='paper-detail'),
    path('<slug:slug>', views.PaperDetailView.as_view(), name='paper-detail'),
    path('paper-favorite/', views.AddPaperFavorite.as_view(), name='paper-favorite')
]