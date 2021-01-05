from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Article
# Create your tests here.



class Articles_Test(TestCase):
    def setUp(self):
        
        self.user = get_user_model().objects.create_user(
            username = 'aghyad',
            email='aghyad@admin.com',
            password = 'aghyad@123456'
        )
        
        self.fake_article = Article.objects.create(
            title = 'python for everyone',
            author = self.user,
            body = '401 Advance course'        
            
        )
        
        
    def test_article_page_status(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code,200)
        
    def test_article_details_status(self):
        res = self.client.get(reverse('article_page', args='1'))
        self.assertEqual(res.status_code, 200)
        
    def test_article_details_content(self):
        res = self.client.get(reverse('article_page', args='1'))
        self.assertContains(res, '401')
        
    def test_article_update(self):
        res = self.client.post(reverse('article_update', args='1'), {
            'title': 'p4e',
        })
        self.assertContains(res, 'p4e')
    
    def test_article_delete(self):
        res = self.client.post(reverse('article_delete', args='1'))
        self.assertEqual(res.status_code,302)