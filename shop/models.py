from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="식당이름")
    image = models.ImageField()
    content = models.TextField(max_length=500, verbose_name="내용")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)


    class Meta:
        ordering=['-id']
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

   