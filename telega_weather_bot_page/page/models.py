from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
