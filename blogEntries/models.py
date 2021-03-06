from django.db import models

from django.contrib.auth.models import User

# Create your models here. The database model. 

class BlogEntry(models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "blogEntries"

    def __str__(self):
        return f'{self.entry_title}'