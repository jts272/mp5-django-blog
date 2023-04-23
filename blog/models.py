from django.db import models

# Our imports
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Tuple for our status
STATUS = ((0, 'Draft'), (1, 'Published'))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # If one record is deleted in the one-to-many, related records are
    # deleted too. Delete User = delete their blog posts
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # Use our STATUS tuple here
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        # Use this to order our posts by creation date
        # '-' means in descending order
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    # ForeignKey = one-to-many
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # Don't forget helper methods
    class Meta:
        # No '-' means it is in standard order - oldest first
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
