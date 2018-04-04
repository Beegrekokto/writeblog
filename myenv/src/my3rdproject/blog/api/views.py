from .serializers import BlogPostSerializer
from rest_framework import generics
from blog.models import BlogPost

class BlogListAPI(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
