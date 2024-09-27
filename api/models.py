from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    # image=models.FileField(upload_to='student_Image')
    image = CloudinaryField('image')