from django.shortcuts import render

# Create your views here.
from .forms import CommentForm
from blog.models import Post, Comment

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)


    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #form is then validated using is_valid(). If the form is valid,
            #  a new instance of Comment is created. You can access 
            # the data from the form using form.cleaned_data, which is a dictionary.
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()


    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form":form,
    }

    return render(request, "blog_detail.html", context)    





