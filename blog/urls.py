# Create our urls for the blog app
from . import views
from django.urls import path


urlpatterns = [
    # as_view() method required to render the class as a view
    path('', views.PostList.as_view(), name='home')
]
