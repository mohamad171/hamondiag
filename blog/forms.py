from django import forms
from blog.models import Blog
# ,Picture,Text


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["name", "picture", "content"]
