from django.urls import path
from .views import GenericAPIView

urlpatterns = [ 
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]