from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Favorites(models.Model):
    owner = models.ForeignKey('auth.User', related_name='favorites_owner', on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, related_name='favorites', on_delete=models.CASCADE)


class Comment(models.Model):
    owner = models.ForeignKey('auth.User', related_name='comment_owner', on_delete=models.CASCADE)
    post = models.ForeignKey(Todo, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} --> {self.post}'
