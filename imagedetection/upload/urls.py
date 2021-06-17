from django.urls import path
from . import views

app_name = 'upload'
urlpatterns = [
path('',views.UploadImage.as_view(),name="upload"),
path('detectedimage/<int:pk>',views.ShowImage.as_view(), name = "detectedimage"),
]