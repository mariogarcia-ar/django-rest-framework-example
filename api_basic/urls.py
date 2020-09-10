from django.urls import path
from .views import GenericAPIView

urlpatterns = [ 
    path('generic/document/', GenericAPIView.as_view()),
    path('generic/document/<int:id>/', GenericAPIView.as_view()),
]