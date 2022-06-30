from django import forms
from .models import Post, blog

class PostForm(forms):
    class Meta:
        model = Post
        fields = [
            "title",
            "author",
            "body"
            ]