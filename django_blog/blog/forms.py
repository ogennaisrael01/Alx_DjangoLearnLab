from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from blog.models import Post, Comment, Tag

CustomUser = get_user_model()

class RegisterForm(UserCreationForm):
   
    class Meta:
        model = CustomUser
        fields = ["email", "username", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    def clean(self):
        if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("Passwords do not match.")
        return self.cleaned_data

class CreatePostForm(forms.ModelForm):
    # Create a tag field 

    tag = forms.ModelMultipleChoiceField(Tag.objects.all(), required=False)
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def clean_tag(self):
        tags = self.cleaned_data["tag"]
        for tag in tags:
            if Post.objects.filter(tag__name=tag).exists():
                raise forms.ValidationError(f"Tag '{tag}' already exists")
        return tags

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content:
            raise forms.ValidationError("Fill out the content")
        
        if len(content) > 100:
            raise forms.ValidationError("Content cannot be grater than 100 words")
        return content
    
        
class SearchForm(forms.ModelForm):
    # tag = forms.CharField(max_length=100)
    class Meta:
        model = Post
        fields = ["title"]
