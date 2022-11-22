from django.shortcuts import render, HttpResponse
from .models import *
from django.core.paginator import Paginator


def search_view(request):
    # base objects
    posts_pop = Article.objects.all().order_by('-views')[:3]
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))
    # main
    if request.method == 'POST':
        q = request.POST.get('q')  # None
        posts = Article.objects.filter(is_published=True).filter(title__contains=q)
    else:
        return HttpResponse('<h1>Searchga hichnarsa yozilmadi</h1>')
    context = {
        # base
        'cats': cats,
        'zone_cat': zone_cat,
        # 'posts_car': posts[:3:-1],
        'posts_pop': posts_pop,
        # main
        'posts': posts,
        'cat': q,
    }
    return render(request, 'category.html', context)


def category_view(request, pk):
    # base objects
    posts_pop = Article.objects.all().order_by('-views')[:3]
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))
    # main
    cat = Category.objects.get(id=pk)
    posts = Article.objects.filter(cat=cat).filter(is_published=True)

    context = {
        # base
        'cats': cats,
        'zone_cat': zone_cat,
        'posts_car': posts[:3:-1],
        'posts_pop': posts_pop,
        # main
        'posts': posts,
        'cat': cat,
    }
    return render(request, 'category.html', context)


def detail(request, slug):
    # base objects
    posts_pop = Article.objects.all().order_by('-views')[:3]
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    posts = Article.objects.filter(is_published=True)
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))

    # main
    obj = Article.objects.get(slug=slug)
    obj.views += 1
    obj.save()

    context = {
        # base
        'cats': cats,
        'zone_cat': zone_cat,
        'posts_car': posts[:3:-1],
        'posts_pop': posts_pop,
        # main
        'obj': obj,
    }
    return render(request, 'blog-single.html', context)


def home(request):
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    posts = Article.objects.filter(is_published=True)
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))
    p = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    context = {
        'cats': cats,
        'zone_cat': zone_cat,
        'p': p,
        'posts': posts_,
        'posts_car': posts[:3:-1],
    }

    return render(request, 'index.html', context)


def about_view(request):
    return render(request, 'about.html')
