from django.db import models

class CreateNotice(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    announcement = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['created']