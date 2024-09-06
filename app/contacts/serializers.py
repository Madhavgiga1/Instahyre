from rest_framework import serializers
from core.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'phone_number', 'name', 'associated_user']
        read_only_fields = ['associated_user']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['associated_user'] = request.user
            return super().create(validated_data)
        else:
            raise serializers.ValidationError('You must be authenticated to create a contact.')