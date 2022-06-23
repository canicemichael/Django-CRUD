from django.urls import path
from blog import views
from blog.views import MyView, PostListView

urlpatterns = [
    path("", views.home, name="home"),
    path('mine/', MyView.as_view(), name="my-view"),
    path("post/", PostListView.as_view(), name="article-list"),
    path("blog/<name>", views.hello_there, name="hello_there"),
]