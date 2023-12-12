from django.db import models
from django.utils.html import mark_safe
class Support_Ticket(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    problem = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/', default="")
    def image_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "250"/>')


