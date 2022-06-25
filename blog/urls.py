from django.urls import path
from blog import views
from blog.views import PostListView, PostCreateView, PostDeleteView, PostUpdateView, PostDetailView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="all"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("delete/<slug:slug>", PostDeleteView.as_view(), name="post_delete"),
    path("update/<slug:slug>", PostUpdateView.as_view(), name="post_update"),
    path("read/<slug:slug>", PostDetailView.as_view(), name="post_detail"),
]