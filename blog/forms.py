from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', "author", "body"]


class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', "body"]
        widgets = {
            'title': forms.TextInput(attrs={'class':
                        'my-input-class'}),
            'body': forms.Textarea(attrs={'class':
                        'my-input-class'}),
        }
