from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Topic(models.Model):
    topic = models.CharField(max_length=200)
    
    def __str__(self):
        return self.topic


class Blog(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.TextField(max_length=200, null=True, blank=True)
    article = RichTextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)    
    
    
    def __str__(self):
        return f'{self.title [0:50]} - created on: {str(self.created)}'

    class Meta:
        ordering = ['-created']