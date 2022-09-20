from django.shortcuts import render

from posts.models import Post, Comment


def main(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    data = {
        'posts': posts,
        'Comment': comments
    }

    return render(request, 'main.html', context=data)

