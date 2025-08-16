from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from blog.models import Post, Comment

CustomUser = get_user_model()

class RegisterForm(UserCreationForm):
    # password1 = forms.CharField(
    #     label="Password",
    #     widget=forms.PasswordInput,
    #     help_text="Enter a strong password.",
    # )
    # password2 = forms.CharField(
    #     label="Confirm Password",
    #     widget=forms.PasswordInput,
    #     help_text="Enter the same password as above, for verification.",
    # )
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
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

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
    
        
