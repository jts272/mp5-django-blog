from django.contrib import admin
# Our imports
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Generate the slug field automatically
    prepopulated_fields = {'slug': ('title',)}
    # Add filtering options to 'Post' in Django admin panel, using
    # fields from our model
    list_filter = ('status', 'created_on')
    # Add fields to the change list in admin panel
    list_display = ('title', 'slug', 'status', 'created_on')
    # Add a search box that searches through the following field names
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']

    # Add a custom 'action' method to the Comment model in admin panel
    # See https://docs.djangoproject.com/en/3.2/ref/contrib/admin/actions/
    # We are providing a list for the method we will define below
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        # Comments are False by default. Now we can approve them
        queryset.update(approved=True)


# Register your models here.
# We won't use conventional method below. We can only add two args so a
# decorator will be used on the class above to register both Post and
# PostAdmin to the admin site
# admin.site.register(Post, PostAdmin)
