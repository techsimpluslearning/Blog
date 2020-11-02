from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

class LikeBlog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, null=True)

class UserComment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE,null=True)
    comment = models.TextField(null=True)

    def __str__(self):
        return self.author.first_name + '--' + self.blog.title