from django.urls import path
from .views import (BlogListView, BlogDetailView, BlogCreateView,
                        blog_create_view, 
                        BlogCreateTemplateView,)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    # path("post/<int:pk>/", BlogDetailTemplateView.as_view(), name="post_detail"),
    path("post/<slug:slug>/", BlogDetailView.as_view(), name="post_detail"),
    # path("post_new/", BlogCreateView.as_view(), name="post_new"),
    # path("post_new/", blog_create_view, name="post_new"),
    path("post_new/", BlogCreateTemplateView.as_view(), name="post_new"),

]