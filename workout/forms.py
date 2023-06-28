from django import forms
from datetime import datetime
from .models import Post, Exercise, Comment
from django.forms import ModelForm



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title','featured_image', 'excerpt',)