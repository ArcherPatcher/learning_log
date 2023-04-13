from django.db import models

# Create your models here.
 
class Topic(models.Model):
 text = models.CharField(max_length=200)
 from django.utils import timezone
 date_added = models.DateTimeField(auto_now_add=timezone.now)
 
def __str__(self):
 
 return self.text
class Entry(models.Model):
 """Информация, изученная пользователем по теме"""
 topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
 text = models.TextField()
 from django.utils import timezone
 date_added = models.DateTimeField(auto_now_add=timezone.now)
 
class Meta:
 verbose_name_plural = 'entries'
 
def __str__(self):
 return f"{self.text[:50]}..."