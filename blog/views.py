from django.shortcuts import render
# import generic library for generic class-based views
from django.views import generic
# Our models that our views are based on
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    # Provide the model to be used
    model = Post
    # Supply the contents of the Post table, where items are published
    # and chronologically ordered
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # We will render the view to this file
    template_name = 'index.html'
    # Limit the number of posts that can appear at once
    paginate_by = 6
