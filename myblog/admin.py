import datetime
from django.contrib import admin
from django.core import urlresolvers  

from myblog.models import Post
from myblog.models import Category


class CategoriesInline(admin.TabularInline):
    model = Category.posts.through
  
def make_published(request, queryset):
    '''
    make_published is a PostAdmin method but I get a global name 
    error without this being defined. However, it does not get called.
    '''
    pass
    
class PostAdmin(admin.ModelAdmin):
    model= Post
    date_hierarchy = 'created_date'
    list_display = ['title', 'author_link', 'created_date', 'modified_date', 'published_date']

    inlines = [
        CategoriesInline,
     ]
    actions = ['make_published']

    def make_published(self, request, queryset):
        print 'It works?'
        rows_updated = queryset.update(published_date=datetime.datetime.now())
        make_published.short_description = "Mark selected posts as published"
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = "%s posts were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    
    def author_link(self, obj):
        return '<a href="%s">%s</a>' % (
            urlresolvers.reverse('admin:auth_user_change', args=(obj.author.id,)), obj.author
            )
    author_link.allow_tags = True
    author_link.short_description = 'Author'

    
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

