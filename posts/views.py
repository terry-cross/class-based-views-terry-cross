from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.views.generic import View 
from posts.forms import LoginForm, PostForm, SignupForm
from posts.models import Post



# @login_required
# def index_view(request):

#     template_name = "index.html"
#     posts = Post.objects.all().order_by("-created_at")
#     context = {"posts": posts}
#     return render(request, template_name, context)


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        template_name = "index.html"
        posts = Post.objects.all().order_by("-created_at")
        context = {"posts": posts}
        return render(request, template_name, context)

# def post_detail_view(request, post_id):
#     template_name = "post_detail.html"
#     post = Post.objects.filter(id=post_id).first()
#     context = {"post": post}
#     return render(request, template_name, context)

class PostDetailView(View):

    def get(self, request, post_id):
        template_name = "post_detail.html"
        post = Post.objects.filter(id=post_id).first()
        context = {"post": post}
        return render(request, template_name, context)


# def user_detail_view(request, user_id):
#     template_name = "user_detail.html"
#     target_user = User.objects.get(id=user_id)
#     posts = Post.objects.filter(creator=target_user)
#     context = {"posts": posts, "target_user": target_user}
#     return render(request, template_name, context)

class  UserDetailView (View):

    def get(self, request, user_id):
        template_name = "user_detail.html"
        target_user = User.objects.get(id=user_id)
        posts = Post.objects.filter(creator=target_user)
        context = {"posts": posts, "target_user": target_user}
        return render(request, template_name, context)


# @login_required
# def create_post_view(request):
#     template_name = "generic_form.html"
#     form = PostForm()

#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             post = Post.objects.create(body=data.get("body"), creator=request.user)
#             return redirect(reverse("post_detail", args=(post.id,)))

#     return render(request, template_name, {"form": form, "header": "Create a Post"})

class CreatePostView(LoginRequiredMixin, View):

    def get(self, request):
        template_name = "generic_form.html"
        form = PostForm()
        return render(request, template_name, {"form": form, "header": "Create a Post"})    

    def post(self, request):
            form = PostForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.create(body=data.get("body"), creator=request.user)
                return redirect(reverse("post_detail", args=(post.id,)))


def signup_view(request):
    template_name = "generic_form.html"
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data.get("username"), password=data.get("password")
            )
            login(request, user)
            return redirect(reverse("homepage"))
    return render(request, template_name, {"form": form, "header": "Signup"})



def login_view(request):
    template_name = "generic_form.html"
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request, user)
                return redirect(request.GET.get("next", "/"))
    return render(request, template_name, {"form": form, "header": "Login"})


def logout_view(request):
    logout(request)
    return redirect(reverse("homepage"))
