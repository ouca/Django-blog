from django.shortcuts import render
from django.views import  View
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import Http404, HttpResponse
from django.views import generic

# Create your views here.
def paginate_queryset(request, queryset, count):

    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

def post_list(request):
    posts = Post.objects.all()
    page_obj = paginate_queryset(request, posts, 12)
    print(page_obj.object_list)
    return render(request, 'bblog/blog.html', {
        'posts': posts,
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
    })


def PostDetail(request, pk):
    article = get_object_or_404(Post,id=pk)
    return render(request, 'bblog/article.html',{
        'article': article
    })

def List_Python(request):
   python_Category = Post.objects.filter(bigCategory__name="python")
   page_obj = paginate_queryset(request, python_Category, 1)
   print(page_obj.object_list)
   return render(request, 'bblog/python.html', {
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
                                })

def List_docker(request):
   docker_Category = Post.objects.filter(bigCategory__name='docker')
   page_obj = paginate_queryset(request, docker_Category, 1)
   print(page_obj.object_list)
   return render(request, 'bblog/docker.html', {
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
                                })
