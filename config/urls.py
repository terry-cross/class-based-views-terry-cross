"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', include('home.urls')),
    
    # path("", views.index_view, name="homepage"),
    path("", views.IndexView.as_view(), name="homepage"),

    # path("post/<int:post_id>/", views.post_detail_view, name="post_detail"),
    path("post/<int:post_id>/", views.PostDetailView.as_view(), name="post_detail"),

    # path("user/<int:user_id>/", views.user_detail_view, name="homepage"),
    path("user/<int:user_id>/", views.UserDetailView.as_view(), name="homepage"),

    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),

    # path("post/create/", views.create_post_view, name="create"),
    path("post/create/", views.CreatePostView.as_view(), name="create"),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
