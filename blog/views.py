from django.shortcuts import render, get_object_or_404
# import generic library for generic class-based views
from django.views import generic, View
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


class PostDetail(View):
    # Method to display posts
    def get(self, request, slug, *args, **kwargs):
        # Get the posts, starting with active posts only
        queryset = Post.objects.filter(status=1)
        # Pass in the slug to identify the post we want
        post = get_object_or_404(queryset, slug=slug)
        # Get the post's comments
        comments = post.comments.filter(approved=True).order_by('created_on')
        # Set bool to check if logged in user liked the post
        liked = False
        # If logged in user has liked the post, set to True
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            # Context object
            {
                'post': post,
                'comments': comments,
                'liked': liked
            }
        )
