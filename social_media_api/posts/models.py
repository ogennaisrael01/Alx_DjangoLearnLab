from django.db import models
from django.conf import settings
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post made by {self.author.username} on {self.created_at}"
    
    def get_absolute_url(self):
        return reverse("post-detail", args=str(self["pk"]))
    
class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment made by {self.author.username} On the post titled {self.post.title}"
    
