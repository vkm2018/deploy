from rest_framework import serializers

from applications.account.tasks import spam_email
from applications.spam.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


    def create(self, validated_data):

        email = Contact.objects.all(validated_data)
        spam_email.delay(email)
        return email
