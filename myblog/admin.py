from django.contrib import admin
from myblog.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

# class CategoryInline(admin.TabularInline):
    # model = Category.posts.through  
    
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )
    
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
    # exclude = ('posts',)
    
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
    # inlines = [CategoryInline]
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

