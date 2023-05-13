import datetime as dt

from django.shortcuts import get_list_or_404, get_object_or_404, render

from blogicum import constants
from blog.models import Post


def index(request):
    post_list = Post.objects.select_related(
        'category', 'author', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=dt.datetime.now(dt.timezone.utc),
    )[:constants.POSTS_ON_MAIN]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=dt.datetime.now(dt.timezone.utc),
        ),
        pk=id,
    )
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    post_list = get_list_or_404(
        Post.objects.select_related(
            'category', 'author', 'location'
        ).filter(
            is_published=True,
            category__is_published=True,
            category__slug=category_slug,
            pub_date__lte=dt.datetime.now(dt.timezone.utc),
        )
    )
    context = {
        'category': category_slug,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
