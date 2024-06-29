from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator

class Post(models.Model):
  title = models.CharField(max_length=100)
  rating = models.IntegerField(default=0,validators=[MinLengthValidator(1), MaxValueValidator(5)])
  content = models.TextField()
  author = models.CharField(null=True,max_length=100)
  is_liked = models.BooleanField(default=False)

  def __str__(self):
    return F"{self.title} - {self.content}"
