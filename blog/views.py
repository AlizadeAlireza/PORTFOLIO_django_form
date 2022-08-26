from multiprocessing import context
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm, SearchForm
# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')

    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        SearchText = searchForm.cleaned_data['SearchText']
        posts = posts = Post.objects.filter(title__contains=SearchText).order_by('-created_on')
    else:
        posts = Post.objects.all().order_by('-created_on')

    context = {
        "posts": posts,
        "searchForm": searchForm
    }
    return render(request, "blog/blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')

    context = {
        "category": category,
        "posts": posts,
    }
    
    return render (request, "blog/blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk = pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()

    comments = Comment.objects.filter(post = post)

    context = {
        'post': post,
        "comments": comments, 
        "form":form
    }
    
    return render(request, "blog/blog_detail.html", context)