from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.core.paginator import Paginator
from django.utils import timezone
from .forms import BlogUpdate
from faker import Faker
# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    #paginator : 글을 몇 개 단위로 볼거다
    paginator = Paginator(blog_list, 5)
    #request된 페이지를 page 변수에 담는다
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'articles':articles})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.editor = str(request.user.username)
    blog.save()
    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    Blog.objects.get(id=blog_id).delete()
    return redirect('/')

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date = timezone.now()
            blog.editor = str(request.user.username)
            blog.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)
        return render(request,'update.html', {'form':form})

def fake(request):
    for i in range(5) :
        blog = Blog()
        myfake = Faker()
        blog.title = myfake.sentence()
        blog.body = myfake.text()
        blog.pub_date = timezone.datetime.now()
        blog.editor = str(request.user.username)
        blog.save()
    return redirect('/')
    

