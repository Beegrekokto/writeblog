from django.urls import path
from .models import BlogPost
from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from .views import Home, Create_blog, About, Contact, BlogDetail, Delete, SignUp

urlpatterns = [
    path('', Home, name = 'home'),
    path('create_blog/', Create_blog, name = 'create_blog'),
    path('about/', About, name = 'about'),
    path('contact/', Contact, name = 'contact'),
    path('login/', login, {'template_name': 'login.html'}, name = 'login'),
    path('logout/', logout, name='logout'),
    path('signup/', SignUp, name = 'signup'),
    url(r'^blogdetail/(?P<id>\d+)/$', BlogDetail, name = 'blogdetail'),
    url(r'^delete/(?P<id>\d+)/$', Delete, name = 'delete'),
    path('api/', include('blog.api.urls')),



]
