from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from applications.spam.models import Contact
from applications.spam.serializers import ContactSerializer


class ContactView(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]


#TODO: реализовать отправку спам сообщений всем объектам из модели Contact,
# при создании товара отправлять сообщение в всем объектам из модели Contact

