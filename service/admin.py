from django.contrib import admin
from .models import *

# загоовки страницы
class ServiceMeinTitleAdmin (admin.ModelAdmin):
    #  вывод всех полей в админку
      list_display = [field.name for field in ServiceMeinTitle._meta.fields]

class Meta:
    model = ServiceMeinTitle
admin.site.register(ServiceMeinTitle,ServiceMeinTitleAdmin)

# сервисы на странице
class ServiceAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Service._meta.fields]

class Meta:
    model = Service
admin.site.register(Service,ServiceAdmin)

# сервисы_2 на странице
class ServiceSecondAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in ServiceSecond._meta.fields]

class Meta:
    model = ServiceSecond
admin.site.register(ServiceSecond,ServiceSecondAdmin)

class ServiceImgAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in ServiceImg._meta.fields]

class Meta:
    model = ServiceImg
admin.site.register(ServiceImg,ServiceImgAdmin)
