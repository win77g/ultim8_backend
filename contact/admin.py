from django.contrib import admin
from .models import *
# Register your models here.
class QuestAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку

   list_display = ['name','email','phone','message','control']



class Meta:
    model = Quest
# Register your models here.
admin.site.register(Quest,QuestAdmin)
