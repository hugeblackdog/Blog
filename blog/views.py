from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post, Category
import markdown


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html',
                  # 传递参数得用字典
                  context={
                      'posts': posts,
                  })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'posts': posts})


def archives(request, year, month):
    posts = Post.objects.filter(created_time__year=year,
                                created_time__month=month
                                ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'posts': posts})
