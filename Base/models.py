from django.db import models

# Create your models here.

class Topic(models.Model):
    topic = models.CharField(max_length=200)
    
    def __str__(self):
        return self.topic


class Blog(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.TextField(max_length=200, null=True, blank=True)
    article = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)    
    
    
    def __str__(self):
        return self.title + " - " + self.article [0:50] + " ..."

    class Meta:
        ordering = ['-created']