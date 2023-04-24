from django.contrib import admin
# Our imports
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


# Register your models here.
# We won't use conventional method below. We can only add two args so a
# decorator will be used on the class above to register both Post and
# PostAdmin to the admin site
# admin.site.register(Post, PostAdmin)
