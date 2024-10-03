from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

def validate_video_file(file):
    max_size = 104857600  # 100MB
    if file.size > max_size:
        raise ValidationError("Max file size is 100MB.")
    if not file.name.lower().endswith(('.mp4', '.mov', '.avi', '.wmv', '.flv', '.mkv')):
        raise ValidationError("Unsupported file extension.")


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video= CloudinaryField('video', resource_type='video')  
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=200,null=True)
    # duration = models.DurationField()