from django import forms
from .models import Blog
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('user',)  
