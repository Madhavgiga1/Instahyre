from rest_framework import serializers
from core.models import Spam
class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spam
        fields = ['phone_number', 'reporting_user']