from django.shortcuts import render, get_object_or_404
# import generic library for generic class-based views
from django.views import generic, View
# Our models that our views are based on
from .models import Post
# Import our CommentForm class
from .forms import CommentForm

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
                'commented': False,
                'liked': liked,
                # Add our CommentForm to the context to render
                # Will be rendered in the post_detail template
                'comment_form': CommentForm()
            }
        )

        # Post method - as in HTTP post method when user adds a comment
        # This is a copy of the `get` method with adjustments
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Get the data from our form
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            # Get the comment, but don't commit to the db yet
            comment = comment_form.save(commit=False)
            # Assign a post to the comment, so we know which post the
            # comment has been left on
            comment.post = post
            comment.save()
        else:
            # Return empty comment form instance
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            # Context object
            {
                'post': post,
                'comments': comments,
                # Add a commented value and set it to True
                # This will be used to notify users their comment is
                # awaiting approval in `post_detail.html``
                # Corresponding False value added to `get` method
                'commented': True,
                'liked': liked,
                # Add our CommentForm to the context to render
                # Will be rendered in the post_detail template
                'comment_form': CommentForm()
            }
        )
