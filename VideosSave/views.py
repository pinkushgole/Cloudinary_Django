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
    # def post (self,request):
    #     title = request.POST.get('title')
    #     description = request.POST.get('description', '')
    #     video_file = request.FILES.get('video')

    #     # Basic Validation
    #     if not title:
    #         messages.error(request, 'Title is required.')
    #         return redirect('videos')
        
    #     if not video_file:
    #         messages.error(request, 'No video file selected.')
    #         return redirect('videos')
    #     try:
    #             # Manual validation
    #         validate_video_file(video_file)
    #         video = Video.objects.create(
    #                 title=title,
    #                 description=description,
    #                 video=video_file
    #             )
    #         messages.success(request, 'Video uploaded successfully!')
    #         return redirect('/videos')
    #     except Exception as e:
    #         messages.error(request, f'An error occurred: {str(e)}')
    #         return redirect('/videos')
    


# class VideoData(APIView):
#     
    
   