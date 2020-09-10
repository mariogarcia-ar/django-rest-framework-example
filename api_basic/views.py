from .models import Document
from .serializers import DocumentSerializer
from rest_framework import generics
from rest_framework import mixins
# import logging



class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    lookup_field = 'id'

  

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)

        else:
           return self.list(request)

    def post(self, request):
        # logger = logging.getLogger("info")
        # logger.info(request.body)
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)