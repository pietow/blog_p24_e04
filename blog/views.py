from django.shortcuts import render, Http404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
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

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title', "author", "body"]


from django.forms import ModelForm
from django.shortcuts import redirect

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', "author", "body"]

class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', "body"]

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
