from django.shortcuts import render, get_object_or_404

from .models import Post, Group

NUMBER_OF_POSTS_DISPLAYED = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:NUMBER_OF_POSTS_DISPLAYED]
    context = {
        'posts': posts,
        'button': 'все записи группы',
        'title': 'Последние обновления на сайте'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all().order_by('-pub_date')[:NUMBER_OF_POSTS_DISPLAYED]
    context = {
        'group': group,
        'posts': posts,
        'title_group_list': 'Записи сообщества'
    }
    return render(request, 'posts/group_list.html', context)
