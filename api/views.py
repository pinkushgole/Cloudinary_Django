from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer
from django.shortcuts import get_object_or_404

class StudentAdd(APIView):
    def get(self, request, format=None):
        photos = Student.objects.all()
        serializer = StudentSerializer(photos, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PhotoDetailAPIView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Photo, pk=pk)

#     def get(self, request, pk, format=None):
#         photo = self.get_object(pk)
#         serializer = PhotoSerializer(photo, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk, format=None):
#         photo = self.get_object(pk)
#         serializer = PhotoSerializer(photo, data=request.data, partial=True, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         photo = self.get_object(pk)
#         photo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
