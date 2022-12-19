from .views import FileView
from django.urls import path,include

urlpatterns = [
    path('', FileView.as_view(), name='file-upload'),
]