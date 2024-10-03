# superuser : pinkush pass: 12345
from django.contrib import admin
from django.urls import path
from api import views as api
from VideosSave import views as vs
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addstudent/', api.StudentAdd.as_view()),
    path('videos/', vs.videos.as_view(),name="videos"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)