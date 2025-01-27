from django.urls import path
from .views import BlogListView, BlogDetailTemplateView, BlogDetailView, blog_detail_view

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    # path("post/<int:pk>/", BlogDetailTemplateView.as_view(), name="post_detail")
    path("post/<slug:slug>/", BlogDetailView.as_view(), name="post_detail")
]