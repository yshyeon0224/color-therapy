from django.db import models

# Create your models here.
class Colors(models.Model):
    color_name = models.CharField(max_length=20)
    color_image = models.ImageField(upload_to='color_images/%Y/%m/%d/', null=True, blank=True)
    color_ex = models.TextField

