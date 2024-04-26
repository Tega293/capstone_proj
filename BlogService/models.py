from django.db import models
from UserService.models  import CustomUser

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
class Tags(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='blog title', unique=True)
    description = models.TextField()
    content = models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    thumbnail=models.ImageField(upload_to = 'thumbnail' )
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    author=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   

    def __str__(self) -> str:
        return f"{self.title}"