from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    """A model representing Blog Posts"""
    title=models.CharField(max_length=200)
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('BlogAuthor',on_delete=models.SET_NULL, null = True)
    description = models.TextField(max_length=1000,help_text="Contents of the actual post")

    class Meta:
        ordering = ['-post_date']
    
    def get_absolute_url(self):
        """Returns the url to access a particular blog instance."""
        return reverse('blog-detail',args=[str(self.id)])

    def __str__(self):
        return self.title

class Comment(models.Model):
    """Comments for each blog post"""
    comment = models.TextField(max_length=200,help_text='Enter comment about blog post here.')
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    blog = models.ForeignKey('Blog',on_delete=models.SET_NULL,null=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.comment

class BlogAuthor(models.Model):
    """Model representing Bloggers"""
    name = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    bio = models.CharField(max_length=1000,null=True,blank=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('blogauthor-detail',args=[str(self.id)])

    def __str__(self):
        return self.name.username