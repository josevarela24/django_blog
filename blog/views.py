from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Joey",
        "title": "Blog Post",
        "content": "First post content",
        "date_posted": "December 21, 2019",
    },
    {
        "author": "Alice",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "January 21, 2020",
    },
]

# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})

