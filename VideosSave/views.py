from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import messages
from .models import Video,validate_video_file
from django.core.exceptions import ValidationError
from .serializer import VideoSerializer

# Create your views here.


class videos(APIView):
    def get(self,request):
        videos = Video.objects.all().order_by('-uploaded_at')
        return render(request, 'addvideos.html', {'videos': videos})
    
    def post(self, request, format=None):
        serializer = VideoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Video uploaded successfully!')
            return redirect('/videos')
        return redirect('/videos')
   