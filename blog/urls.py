from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.BlogList.as_view(), name='blog-list'),
    path('bloggers/',views.BlogAuthorList.as_view(), name='blogauthor-list'),
    path('bloggers/<int:pk>',views.BlogAuthorDetail.as_view(),name='blogauthor-detail'),
    path('<int:pk>/',views.BlogDetail.as_view(),name='blog-detail'),
    path('<int:pk>/create',views.newComment,name='comment_create'),
]