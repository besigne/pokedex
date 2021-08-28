from rest_framework.viewsets import ModelViewSet
from core.model.type import Type
from core.serializer.type_serializer import TypeModelSerializer


class TypeModelViewSet(ModelViewSet):

    queryset = Type.objects.all()
    serializer_class = TypeModelSerializer
