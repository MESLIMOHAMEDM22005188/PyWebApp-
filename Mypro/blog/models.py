from django.db import models

# Create your models here.
class Article(models.Model):
    objects = None
    title= models.CharField(max_length=50)
    desc=models.TextField()
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
