from django.db import models

# Create your models here.
class PageVisit(models.Model):
    page = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.page