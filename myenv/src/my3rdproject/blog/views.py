from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import BlogPost
from .forms import BlogPostForm, SignUPForm

# Create your views here.
# function based views for blog viewing and deleting and creating.
def Home(request):
    blogs = BlogPost.objects.all()
    return render(request, 'index.html', {'blogs':blogs})


def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')


# def Try(request, id):
#     blog = BlogPost.objects.get(id=id)
#     return render(request, 'try.html', {'blog':blog})


def BlogDetail(request, id):
    blog = BlogPost.objects.get(id = id)
    return render(request, 'post.html', {'blog': blog})

def Delete(request, id):
    blog = BlogPost.objects.get(id = id)
    blog.delete()
    return redirect('home')



def Create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = BlogPostForm()

    return render(request, 'create_blog.html', {'form': form})


def SignUp(request):
    if request.method == 'POST':
        form = SignUPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUPForm()
    return render(request, 'registration/signup.html', {'form':form})
