# superuser : pinkush pass: 12345
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addstudent/', views.StudentAdd.as_view()),

]
