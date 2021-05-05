from django.shortcuts import render

from .models import Post
# Create your views here.
def blog_list(request):

    posts = Post.objects.all()

    context = {
        'posts': Post
    }

    return render(request, 'blog/index.html', context)
