from django.urls import path
from .views import GenericAPIView

urlpatterns = [ 
    path('api/document', GenericAPIView.as_view()),
    path('api/document/<int:id>', GenericAPIView.as_view()),
]