
from django.shortcuts import render, HttpResponseRedirect
from myself.models import Post
from myself.forms import PostForm
import datetime


# Create your views here.

def index(request):
    my_dict = dict()
    my_dict["name"] = "Nikita"
    my_dict["fruits"] = ["apple", "banana", "strawberry"]

    my_dict["all_posts"] = Post.objects.all()


    return render(request, 'Index.html', my_dict)

def new_post(request):

    if request.method == 'POST':
        filled_form = PostForm(request.POST)
        post = filled_form.save(commit=False)
        post.date = datetime.datetime.now()
        post.save()
        return HttpResponseRedirect('/myself')

    data = dict()
    data["post_form"] = PostForm()
    return render(request, 'new_post.html', data)

