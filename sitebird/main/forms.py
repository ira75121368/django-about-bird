from django import forms
from .models import Bird, Categories

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ['title', 'slug', 'content', 'category', 'in_the_red_book']

