from django.contrib import admin
from .models import *

# загоовки страницы
class SubscribeAdmin (admin.ModelAdmin):
    #  вывод всех полей в админку
      list_display = [field.name for field in Subscribe._meta.fields]

class Meta:
    model = Subscribe
admin.site.register(Subscribe,SubscribeAdmin)
# Register your models here.
