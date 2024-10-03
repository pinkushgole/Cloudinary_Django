from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import messages
from .models import Video,validate_video_file
from django.core.exceptions import ValidationError
from .serializer import VideoSerializer
from moviepy.editor import VideoFileClip
from datetime import timedelta
# Create your views here.

from django.http import JsonResponse
import json

def track_time(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tracked_time = data.get('time')
        print(f'Tracked Time: {tracked_time} seconds')  # Process or store the tracked time as needed
        return JsonResponse({'status': 'success', 'time': tracked_time})
    
class videos(APIView):
    def get(self,request):
        videos = Video.objects.all().order_by('-uploaded_at')
        return render(request, 'addvideos.html', {'videos': videos})
    
    def post(self, request, format=None):
        data = request.data
        video_file = self.request.FILES.get('video')
        with VideoFileClip(video_file.temporary_file_path()) as video:
            duration_seconds = video.duration
        duration = timedelta(seconds=duration_seconds)

        # Assign duration to data
        data['duration'] = str(duration)
        serializer = VideoSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Video uploaded successfully!')
            return redirect('/videos')
        return redirect('/videos')
   