from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self, hhhhj, hh):
        return self.title

