from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.

class ServiceMeinTitle(models.Model):
      firsttitle = models.CharField(max_length=120,blank=True, null=True, default=None)
      secondtitle = models.CharField(max_length=100,blank=True, null=True, default=None)
# вывод одного поля
      def __str__(self):
          return "Заголовок "
      class Meta:
          verbose_name = 'Загоовок'
          verbose_name_plural = 'Заголовки'


class Service(models.Model):
      title = models.CharField(max_length=100,blank=True, null=True, default=None)
      description = models.TextField(max_length=200,blank=True, null=True, default=None)
      icon = models.CharField(max_length=100,blank=True, null=True, default=None)
# вывод одного поля
      def __str__(self):
          return "Сервисы "
      class Meta:
          verbose_name = 'Сервис'
          verbose_name_plural = 'Сервисы'

class ServiceSecond(models.Model):
      title = models.CharField(max_length=100,blank=True, null=True, default=None)
      description = models.TextField(max_length=200,blank=True, null=True, default=None)
      icon = models.CharField(max_length=100,blank=True, null=True, default=None)
# вывод одного поля
      def __str__(self):
          return "Сервисы_2 "
      class Meta:
          verbose_name = 'Сервис_2'
          verbose_name_plural = 'Сервисы_2'



class ServiceImg(models.Model):
      img = models.ImageField(upload_to='static', blank=True, null=True, default=None)
# вывод одного поля
      def __str__(self):
          return "Сервис фото "
      class Meta:
          verbose_name = 'Сервис фото'
          verbose_name_plural = 'Сервисы фото'

# метод удоения фото из сервера
@receiver(post_delete, sender=ServiceImg)
def submission_delete(sender, instance, **kwargs):
    instance.img.delete(False)
