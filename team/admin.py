from django.contrib import admin
from .models import *

class TeamAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Product._meta.fields]
   #    inlines = [ProductImageInline]
   list_display = ['name','image_img','profesia','description']
   readonly_fields = ['image_img',]
   # fields = ['category', 'title', 'slug', 'metakey', 'metadesc', 'text_redactor', 'text_redactor_full', 'tag', 'timestamp', 'autor', 'image', 'image_img', 'body', 'likes', 'dislikes']

class Meta:
    model = Team
# Register your models here.
admin.site.register(Team,TeamAdmin)
# Register your models here.
