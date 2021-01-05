from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.


class Home_page(ListView):
    template_name = 'home.html'
    model = Article
    
    
class Article_page(DetailView):
    template_name = 'article_content.html'
    model = Article
    
class ArticleCreateView(CreateView):
    template_name ='article_create.html'
    model = Article
    fields = ['title','author','body']
    
class ArticleUpdateView(UpdateView):
    template_name ='article_update.html'
    model = Article
    fields = ['title','author','body']
    
    
    
class ArticleDeleteView(DeleteView):
    template_name ='article_delete.html'
    model = Article
    fields = ['title','author','body']
    success_url = reverse_lazy('home')