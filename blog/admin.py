from django.contrib import admin
from .models import Blog, BlogAuthor, Comment

# Register your models here.
@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    #list_display = ('name')
    fields = ('name','bio')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','blog','comment','post_date')
    list_filter = ('post_date','author','blog')

class CommentInline(admin.TabularInline):
    model = Comment
    extra=0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','post_date')
    list_filter = ('post_date','author')
    inlines = [CommentInline]