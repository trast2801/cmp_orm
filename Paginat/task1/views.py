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

    max_items_per_page = 100  # Максимальное количество элементов на странице
    current_items_per_page = paginator.per_page  # Текущее количество элементов на странице

    context = {
        'posts': posts,
        'paginator': paginator,
        'max_items_per_page': max_items_per_page,
        'current_items_per_page': current_items_per_page
    }
    return render(request, 'index.html', context)

'''def blog_index_custom(request):
    posts = Post.objects.all()
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

    # Дополнительные параметры для пользовательского шаблона пагинации
    max_items_per_page = 10  # Максимальное количество элементов на странице
    current_items_per_page = paginator.per_page  # Текущее количество элементов на странице

    context = {
        'posts': posts,
        'paginator': paginator,
        'max_items_per_page': max_items_per_page,
        'current_items_per_page': current_items_per_page
    }
    return render(request, 'index_custom.html', context)'''



def blog_index_custom(request):
    posts = Post.objects.all()
    num_per_page = int(request.GET.get('num_per_page', 10))
    paginator = Paginator(posts, num_per_page)
    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    context = {'posts': page, 'num_per_page': num_per_page}
    return render(request, 'index_custom.html', context)