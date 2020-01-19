from django.db import models

# Create your models here.
class Subscribe(models.Model):

      email = models.CharField(max_length=200,blank=True, null=True, default=None)

# вывод одного поля
      def __str__(self):
          return "Подписчики "
      class Meta:
          verbose_name = 'Подписчик'
          verbose_name_plural = 'Подписчики'
