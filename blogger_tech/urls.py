from django.contrib import admin
from django.urls import path
from .views import Home_page,Article_page,ArticleCreateView,ArticleUpdateView,ArticleDeleteView

urlpatterns = [
    path('', Home_page.as_view(),name='home'),
    path('<int:pk>',Article_page.as_view(),name='article_page'),
    path('new/',ArticleCreateView.as_view(),name='article_new'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_update'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete')
]
