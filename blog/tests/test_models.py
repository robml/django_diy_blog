from django.test import TestCase
from django.contrib.auth.models import User, Permission

from blog.models import Blog,BlogAuthor,Comment


# Create your tests here

class BlogAuthorTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='dr_evil', password='1X<ISRUkw+tuK')

        test_user1.save()

        BlogAuthor.objects.create(name=test_user1,bio='The brilliant man after Austin Powers')
    
    def test_name_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
    
    def test_bio_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEquals(field_label, 'bio')

    def test_bio_max_length(self):
        author = BlogAuthor.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        self.assertEquals(max_length,1000)
    
    def test_object_name_is_name(self):
        author = BlogAuthor.objects.get(id=1)
        expected_object_name = f'{author.name}'
        self.assertEquals(expected_object_name,str(author))

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='dr_evil', password='1X<ISRUkw+tuK')

        test_user1.save()

        BlogAuthor.objects.create(name=test_user1,bio='The brilliant man after Austin Powers')
        author = BlogAuthor.objects.get(id=1)
        Blog.objects.create(title='First Post',author=author,description="My First Post On Here!")
    
    def test_name_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_post_date_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'post date')
    
    def test_author_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_description_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length,200)
    
    def test_description_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEquals(max_length,1000)
    
    def test_object_name_is_name(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f'{blog.title}'
        self.assertEquals(expected_object_name,str(blog))

class CommentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='dr_evil', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='catman', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        BlogAuthor.objects.create(name=test_user1,bio='The brilliant man after Austin Powers')
        author = BlogAuthor.objects.get(id=1)

        Blog.objects.create(title='First Post',author=author,description="My First Post On Here!")
        blog = Blog.objects.get(id=1)

        Comment.objects.create(comment="Good Job!",author = test_user2,blog=blog)

    def test_comment_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('comment').verbose_name
        self.assertEquals(field_label, 'comment')

    def test_post_date_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'post date')
    
    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_blog_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('blog').verbose_name
        self.assertEquals(field_label, 'blog')
    
    def test_comment_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('comment').max_length
        self.assertEquals(max_length,200)

    def test_object_name_is_name(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'{comment.comment}'
        self.assertEquals(expected_object_name,str(comment))