from django.urls import path
from .views import BlogListAPI

urlpatterns = [
    path('blogdetail-api/', BlogListAPI.as_view(), name = 'blogdetailapi'),

]
