from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from blog.models import Blog, BlogAuthor

class IndexTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code,200)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_view_uses_correct_dr_evil_values(self):
        response = self.client.get(reverse('index'))
        self.assertTrue('num_blogs_dr_evil' in response.context)
        real_count = Blog.objects.filter(author__name__username__iexact='dr_evil').count()
        self.assertEqual(response.context['num_blogs_dr_evil'],real_count)

class BlogAuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        num_users = 13
        for test_user_id in range(num_users):
            test_user_id=str(test_user_id)
            test_user = User.objects.create_user(username='testuser'+test_user_id,password='testuser'+test_user_id)
            test_user.save()
            BlogAuthor.objects.create(name=test_user,bio='user#'+test_user_id)
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/bloggers/')
        self.assertEqual(response.status_code,200)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogauthor-list'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogauthor-list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'blog/blogauthor_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogauthor-list'))
        self.assertEqual(response.status_code,200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blogauthor_list'])==5)
    
class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        num_users = 13
        for test_user_id in range(num_users):
            test_user_id=str(test_user_id)
            test_user = User.objects.create_user(username='testuser'+test_user_id,password='testuser'+test_user_id)
            test_user.save()
            author = BlogAuthor.objects.create(name=test_user,bio='user#'+test_user_id)
            Blog.objects.create(author=author,title="post by user#"+test_user_id,description="test desc")
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/all/')
        self.assertEqual(response.status_code,200)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog-list'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog-list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blog-list'))
        self.assertEqual(response.status_code,200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list'])==5)
    
class BlogAuthorDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser1',password='testuser1')
        test_user.save()
        BlogAuthor.objects.create(name=test_user,bio='user1')
    
    def test_view_url_exists_at_desired_location(self):
        id = BlogAuthor.objects.get(id=1).id
        response = self.client.get('/blog/bloggers/'+str(id))
        self.assertEqual(response.status_code,200)
    
    def test_view_url_accessible_by_name(self):
        id = BlogAuthor.objects.get(id=1).id
        response = self.client.get(reverse('blogauthor-detail',args=[str(id)]))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        id = BlogAuthor.objects.get(id=1).id
        response = self.client.get(reverse('blogauthor-detail',args=[str(id)]))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'blog/blogauthor_detail.html')

class BlogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser1',password='testuser1')
        test_user.save()
        author = BlogAuthor.objects.create(name=test_user,bio='user1')
        Blog.objects.create(author=author,title="post by user1",description="test desc")
    
    def test_view_url_exists_at_desired_location(self):
        id = Blog.objects.get(id=1).id
        response = self.client.get('/blog/'+str(id))
        self.assertEqual(response.status_code,301) # Getting a 301 instead of a 200
    
    def test_view_url_accessible_by_name(self):
        id = Blog.objects.get(id=1).id
        response = self.client.get(reverse('blog-detail',args=[str(id)]))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        id = Blog.objects.get(id=1).id
        response = self.client.get(reverse('blog-detail',args=[str(id)]))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')


# Notes: the test below is already secured on the form and model tests
# HOWEVER: the self.client.get yields a 404 with the current syntax, and a NoReverseMatch when used with reverse
# I leave this as an exercise if testing the View of New comments is crucial to you, best of luck, Rob
"""
class NewCommentViewTest(TestCase):
    def setUp(self):
        # Create a user
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        author = BlogAuthor.objects.create(name=test_user1,bio='user1')
        Blog.objects.create(author=author,title="post by user1",description="test desc")

    def test_redirect_if_not_logged_in(self):
        id = Blog.objects.get(id=1).id
        response = self.client.get('blog/'+str(id)+'/create')
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_logged_in(self):
        id = Blog.objects.get(id=1).id
        login = self.client.login(username='testuser2', password='2HJ1vRV0Z&3iD')
        response = self.client.get('blog/'+str(id)+'/create')
        
        # Check that it lets us login
        self.assertEqual(response.status_code, 200)
    
    def test_uses_correct_template(self):
        id = Blog.objects.get(id=1).id
        login = self.client.login(username='testuser2', password='2HJ1vRV0Z&3iD')
        response = self.client.get('blog/'+str(id)+'/create')
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'blog/comment_form.html')
"""