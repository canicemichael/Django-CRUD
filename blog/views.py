from nntplib import ArticleInfo
from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime


from django.views import View
from django.utils import timezone
from django.views.generic.list import ListView
from blog.models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    paginate_by = 100 # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context




















def home(request):
    return HttpResponse("Hello, Django!")

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World')

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions, URL arguments can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)