from django.shortcuts import render, get_object_or_404, redirect

from main.forms import AddPostForm
from main.models import Bird, Categories


# Create your views here.

def index(request):
    posts = Bird.objects.filter(is_published=1)

    data = {
        'title': 'Главная страница',
        'posts': posts,
    }
    return render(request, 'main/index.html', context=data)


def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'main/about.html', data)

def blog(request):
    posts = Bird.published.all()
    data = {
        'title': 'Статьи о птицах',
        'posts': posts,
    }
    return render(request, 'main/blog.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Bird, slug=post_slug)

    data = {
        'title': post.title,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'main/post.html', data)


def show_category(request, cat_slug):
    category = get_object_or_404(Categories, slug=cat_slug)
    posts = Bird.published.filter(category_id=category.pk)
    data = {
        'title': 'Отображение рубрик',
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'main/blog.html', data)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add')
    else:
        form = AddPostForm()
    data = {
        'title': 'Добавление нового поста',
        'form': form,
    }
    return render(request, 'main/add.html', data)