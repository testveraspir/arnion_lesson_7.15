from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, PaidContent


# Create your views here.

def posts_list(request):
    posts = PaidContent.objects.all()
    return render(request, 'paid_content.html', context = {'posts' : posts})


def post_detail(request, slug):
    post = PaidContent.objects.get(slug__iexact = slug)
    return render(request, 'post_detail.html', context = {'post' : post})


def morph(request):
    return render(request, 'morph.html')


def paid_content(request):
    return render(request, 'paid_content.html')


def index(request):
    return render(request, 'index.html')