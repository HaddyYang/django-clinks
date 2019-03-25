from django.db import models

# Create your models here.
class CustomLink(models.Model):
    text = models.CharField(max_length=64)
    link = models.URLField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<CustomLink: %s>" % self.text

    __unicode__ = __str__ 
