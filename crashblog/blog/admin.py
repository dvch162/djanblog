from django.contrib import admin

from .models import Post, Category, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ('post',)

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'intro', 'body')
    list_display = ('title', 'created_at', 'category', 'slug', 'status')
    list_filter = ('created_at', 'category', 'status')
    inlines = [CommentInline]
    prepopulated_fields = {'slug': ('title',)}



class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'body')
    list_display = ('name', 'created_at', 'post')
    list_filter = ('created_at',)



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
