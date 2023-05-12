from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post
import datetime as dt

END_TIME = dt.datetime.utcnow()


def index(request):
    post_list = Post.objects.select_related(
        'category', 'author', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=END_TIME,
    )[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=END_TIME,
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
            pub_date__lte=END_TIME,
        )
    )
    context = {
        'category': category_slug,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
