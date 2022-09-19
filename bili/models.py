from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chapter(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner_z = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

class Entry(models.Model):
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        n = len(self.text)
        if n > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"
        
class Exercise(models.Model):
    topic = models.CharField(max_length=160, default="none")
    entry = models.ForeignKey(Entry,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        n = len(self.topic)
        if n > 80:
            return f"{self.topic[:80]}..."
        elif n != "none":
            return f"{self.topic}"
        else:
            return f"{self.text[:80]}"