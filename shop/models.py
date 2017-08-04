from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg



class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="식당이름")
    image = models.ImageField()
    content = models.TextField(max_length=500, verbose_name="내용")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    score = models.SmallIntegerField(default=0)


    class Meta:
        ordering=['-id']
    
    def __str__(self):
        return self.title

    @property
    def score_point(self):
        return self.score / 10

    def calc_score(self):
        avg = self.rating_set.all().aggregate(Avg('score'))['score__avg']
        self.score = int(avg * 10)
        self.save()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name


class Rating(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)  # "auth.User"
    shop = models.ForeignKey(Post)
    score = models.SmallIntegerField(default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ])

    class Meta:
        ordering = ['user']



