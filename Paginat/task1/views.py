from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def blog_index(request):
    #posts = Post.objects.all()
    posts = Post.objects.values('title', 'body', 'created_at')
    paginator = Paginator(posts, 2)  # Показывать по 10 постов на странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не целое число, покажем первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше количества страниц, покажем последнюю страницу
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'paginator': paginator,
    }
    return render(request, 'index.html', context)