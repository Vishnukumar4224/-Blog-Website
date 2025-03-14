from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title