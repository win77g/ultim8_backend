from django.contrib import admin
from .models import *

class ArticleBlogAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Product._meta.fields]
   #    inlines = [ProductImageInline]
   list_display = ['name','author','image_img','date','sidebar']
   readonly_fields = ['image_img',]
   # fields = ['category', 'title', 'slug', 'metakey', 'metadesc', 'text_redactor', 'text_redactor_full', 'tag', 'timestamp', 'autor', 'image', 'image_img', 'body', 'likes', 'dislikes']

class Meta:
    model = ArticleBlog
# Register your models here.
admin.site.register(ArticleBlog,ArticleBlogAdmin)

class CommentsAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Product._meta.fields]
   #    inlines = [ProductImageInline]
   list_display = ['name','description','date','email','article']

   # fields = ['category', 'title', 'slug', 'metakey', 'metadesc', 'text_redactor', 'text_redactor_full', 'tag', 'timestamp', 'autor', 'image', 'image_img', 'body', 'likes', 'dislikes']

class Meta:
    model = Comments
# Register your models here.
admin.site.register(Comments,CommentsAdmin)
