from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
def image_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)

class ArticleBlog(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None)
    image = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None)
    description = models.TextField(max_length=200,blank=True, null=True, default=None)
    description_short = models.TextField(max_length=200,blank=True, null=True, default=None)
    author = models.CharField(max_length=120,blank=True, null=True, default=None)
    date = models.DateField(blank=True, null=True, default=None)
    # sidebar = models.CharField(max_length=120,blank=True, null=True, default=None)
    commentari = models.IntegerField(blank=True, null=True, default=None)
    sidebar = models.BooleanField(default=False)


 # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


class Comments(models.Model):
      name = models.CharField(max_length=100,blank=True, null=True, default=None)
      email = models.CharField(max_length=100,blank=True, null=True, default=None)
      description = models.TextField(max_length=200,blank=True, null=True, default=None)
      date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
      article = models.ForeignKey(ArticleBlog,blank=True, null=True, default=None,on_delete=models.CASCADE)
# вывод одного поля
      def __str__(self):
          return "Комментарии "
      class Meta:
          verbose_name = 'Комментарий'
          verbose_name_plural = 'Комментарии'
