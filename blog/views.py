from django.shortcuts import render, Http404, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

class BlogListView(ListView):
    template_name = "home.html"
    model = Post

class BlogDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post

def blog_detail_view(request, pk):
    print(pk)
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404('Post not found')
    return render(request, 'post_detail.html', {'post': post})

class  BlogDetailTemplateView(TemplateView):
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        print(kwargs)
        pk = kwargs.get('pk')
        # try:
        #     post = Post.objects.get(id=pk)
        # except Post.DoesNotExist:
        #     raise Http404('Post not found')
        post = get_object_or_404(Post, pk=pk)
        return {'post': post}



