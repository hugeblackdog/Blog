from django.contrib import admin

# Register your models here.


from .models import Category, Tag, Post


class myCategory(admin.ModelAdmin):
    list_display = ['id', 'name']


class myTag(admin.ModelAdmin):
    list_display = ['id', 'name']


class myPost(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'modified_time', 'category']
    search_fields = ['category', 'tags']
    list_filter = ['category', 'tags']


admin.site.register(Category, myCategory)
admin.site.register(Tag, myTag)
admin.site.register(Post, myPost)
