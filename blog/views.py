from django.shortcuts import render

from .models import Post
# Create your views here.
def blog_list(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/index.html', context)


def blog_details(request, slug):

    posts = Post.objects.get(slug=slug)

    context = {
        'post': posts

    }

    return render(request, 'blog/details.html', context)
