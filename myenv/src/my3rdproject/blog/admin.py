from django.contrib import admin
from .models import BlogPost
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'author', 'created_at']



class BlogPostResource(resources.ModelResource):
    class Meta:
        model = BlogPost

# admin.site.register(BlogPost,)


@admin.register(BlogPost)
class BlogPostAdmin(ImportExportModelAdmin):
    pass
