from django.contrib import admin

from myblog.models import Post
from myblog.models import Category


class CategoriesInline(admin.TabularInline):
    model = Category.posts.through
   # # raw_id_fields = ("Category",)
    
class PostAdmin(admin.ModelAdmin):
   model= Post
   inlines = [
        CategoriesInline,
     ]
    
    
# class CategoryAdmin(admin.ModelAdmin):
    # pass
    
admin.site.register(Post, PostAdmin)
# #admin.site.register(Category, CategoryAdmin)

