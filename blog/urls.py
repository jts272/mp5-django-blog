# Create our urls for the blog app
from . import views
from django.urls import path


urlpatterns = [
    # as_view() method required to render the class as a view
    path('', views.PostList.as_view(), name='home'),
    # Slug comes from the PostDetail view args
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like')
]
