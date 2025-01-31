from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .forms import PostForm, PostUpdateForm
from .models import Post


class ThemeView(View):
    def get(self, request):
        theme = request.session.get('theme', 'light')
        if theme == 'light':
            request.session['theme'] = 'dark'
        else:
            request.session['theme'] = 'light'
        print(request.META.get('HTTP_REFERER'))
        return redirect(request.META.get('HTTP_REFERER'))



class BlogListView(ListView):
    template_name = "home.html"
    model = Post

    def get(self, *args, **kwargs):
        print(self.request.session.get('_auth_user_id'))
        return super().get(*args, **kwargs)

class BlogDetailView(LoginRequiredMixin, DetailView):
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

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title', "author", "body"]

def blog_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "post_new.html", {"form": form})

class BlogCreateTemplateView(TemplateView):
    template_name = "post_new.html"

    def get_context_data(self, **kwargs):
        return {'form': PostForm()}

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response({"form": form})

    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ["title", "body"]


def post_update_view(request, pk):
    post =get_object_or_404(Post, pk=pk) # Post.objects.get(pk=pk)

    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            # print('POST: ',post)
            # print('POST REQUEST: ', request.POST)
            return redirect('post_detail', slug=post.slug)
    elif request.method == "GET":
        form = PostUpdateForm(instance=post)

    return render(request, 'post_edit.html', {'form': form })


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
