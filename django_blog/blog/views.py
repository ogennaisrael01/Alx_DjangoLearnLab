from django.shortcuts import render, redirect
from blog.forms import RegisterForm, CreatePostForm
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post


User = get_user_model()
# Create your views here.


def register(request):
    """ register and save user is user credentials are valid"""

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

class ViewProfile(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "blog/profile.html"
    context_object_name = "user"

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            user_profile = self.model.objects.filter(username=user.username)
            return user_profile
        return None
        

class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "blog/create_post.html"
    success_url = "blogs"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class BlogListView(generic.ListView):
    model = Post
    template_name = "blog/blog_posts.html"
    context_object_name = "blogs"

    def get_queryset(self):
        """ Order blog based on the published recently """
        post = self.model.objects.all().order_by("-published_date")
        return post

        

