from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.models import Blog,BlogAuthor,Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from blog.forms import NewCommentForm

# Create your views here.
class CommentCreate(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ['comment']

class BlogAuthorList(generic.ListView):
    model = BlogAuthor
    paginate_by = 5

class BlogList(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogAuthorDetail(generic.DetailView):
    model = BlogAuthor

class BlogDetail(generic.DetailView):
    model = Blog

@login_required
def newComment(request,pk):
    blog = get_object_or_404(Blog,pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = NewCommentForm(request.POST)

        #Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            new_comment = Comment.objects.create(blog=blog,comment=form.cleaned_data['comment'],author=request.user)
            new_comment.save()

            # redirect to a new URL
            return HttpResponseRedirect(reverse('blog-detail',args=[str(pk)]))
        
    # If this is a GET (or any other method) create the default form.
    else:
        form = NewCommentForm()

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request,'blog/comment_form.html',context=context)

def index(request):
    """View function for the home site"""
    
    # The 'all()' is implied by default
    num_authors = BlogAuthor.objects.count()

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()

    # The 'all()' is implied by default
    num_comments = Comment.objects.all().count()

    # Counter for Posts by Dr. Evil
    try:
        num_blogs_dr_evil = Blog.objects.filter(author__name__username__iexact='dr_evil').count()
    except:
        num_blogs_dr_evil = 0

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1

    context = {
        'num_authors': num_authors,
        'num_blogs': num_blogs,
        'num_comments': num_comments,
        'num_blogs_dr_evil': num_blogs_dr_evil,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)