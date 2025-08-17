from django.shortcuts import render, redirect
from blog.forms import RegisterForm, CreatePostForm, CommentForm
from django.urls import reverse
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post, Comment
from django.shortcuts import get_object_or_404



# Get the custom user model
User = get_user_model()


# Home page view
def home(request):
    return render(request, "blog/home.html")


# User registration view
def register(request):
    """Register and save user if user credentials are valid"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            raise ValueError("Not Valid Input")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", context={
        "form": form
    })


# User profile view, only accessible to logged-in users
class ProfileView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "blog/profile.html"
    context_object_name = "user"

    def get_queryset(self):
        # Return the profile of the currently authenticated user
        user = self.request.user
        if user.is_authenticated:
            user_profile = self.model.objects.filter(username=user.username)
            return user_profile
        return None


# View for creating a new blog post, only for logged-in users
class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "blog/create_post.html"

    def form_valid(self, form):
        # Set the author to the current user before saving
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        # Redirect to the blog list after successful creation
        return reverse("blogs")
    


# View for listing all blog posts, paginated
class PostListView(generic.ListView):
    model = Post
    template_name = "blog/blog_posts.html"
    context_object_name = "blogs"
    paginate_by = 5

    def get_queryset(self):
        """Order blogs based on the most recent published date"""
        post = self.model.objects.all().order_by("-published_date")
        return post

        

# View for displaying details of a single blog post
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/blog_detail.html"
    context_object_name = "blogs"

    def get_queryset(self):
        """Get the comments related to the post"""
        posts = self.model.objects.prefetch_related("post_comment")
        # for post in posts:
        #     for comment in post.post_comment.all():
        #         print(comment.content)
        return posts



# View for updating an existing blog post, only by the author
class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = "blog/update_blog.html"

    def get_queryset(self):
        # Only allow the author to update their own posts
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        # Redirect to the detail view of the updated post
        return reverse("blog-detail", kwargs={"pk": self.object.pk})
    

# View for deleting a blog post, only by the author
class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = "blog/delete_blog.html"
    context_object_name = "blogs"

    def get_queryset(self):
        # Only allow the author to delete their own posts
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        # Redirect to the blog list after deletion
        return reverse("blogs")


# View for creating Comment to a post
class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/create_comment.html"
    context_object_name = "blogs"

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self): 
        return reverse("blog-detail", kwargs={"pk": self.get_object().pk})

class ViewCommentsDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "blog/view_comments.html"
    context_object_name = "blogs"
    paginate_by = 5

# VIew for Editing comment, only by the author
class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/edit_comment.html"
    

    def get_queryset(self):
        # Only the author of a comment can update the comment
        return self.model.objects.filter(author=self.request.user)
    
    def get_success_url(self):
        # Redirect to the detail view of the updated post
        return reverse("blog-detail", kwargs={"pk": self.get_object().pk})
    
class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    template_name = "blog/delete_comment.html"
    context_object_name = "comment"

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
    
    def get_success_url(self):
        return reverse("blogs")
    
    